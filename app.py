"""Initial Flask application for the Job Application Tracker."""

import os
from datetime import date
from decimal import Decimal, InvalidOperation

from flask import Flask, abort, flash, jsonify, redirect, render_template, request, url_for
from mysql.connector.errors import IntegrityError

from database import execute_query, fetch_all, fetch_one, insert_query


app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv(
    "FLASK_SECRET_KEY", "development-key-change-before-deployment"
)


@app.get("/")
def home():
    """Return a basic response while the application is being built."""
    return jsonify({
        "application": "Job Application Tracker",
        "status": "running",
    })


@app.get("/health/database")
def database_health():
    """Check that Flask can run a simple query against MySQL."""
    try:
        result = fetch_one("SELECT 1 AS connected")
        if result and result["connected"] == 1:
            return jsonify({"database": "connected"}), 200
    except Exception as error:
        # Avoid returning connection details or credentials to the client.
        app.logger.error("Database health check failed (%s).", type(error).__name__)

    return jsonify({"database": "unavailable"}), 503


def _company_form_data():
    """Read and normalize company fields submitted from an HTML form."""
    data = {
        "company_name": request.form.get("company_name", "").strip(),
        "industry": request.form.get("industry", "").strip() or None,
        "website": request.form.get("website", "").strip() or None,
        "city": request.form.get("city", "").strip() or None,
        "state": request.form.get("state", "").strip() or None,
        "notes": request.form.get("notes", "").strip() or None,
    }

    errors = []
    if not data["company_name"]:
        errors.append("Company name is required.")
    elif len(data["company_name"]) > 100:
        errors.append("Company name must be 100 characters or fewer.")

    field_limits = {
        "industry": 50,
        "website": 200,
        "city": 50,
        "state": 50,
    }
    for field, limit in field_limits.items():
        value = data[field]
        if value and len(value) > limit:
            errors.append(f"{field.replace('_', ' ').capitalize()} must be {limit} characters or fewer.")

    return data, errors


def _render_companies(edit_company=None, form_values=None, form_errors=None, status=200):
    companies = fetch_all("SELECT * FROM companies ORDER BY company_name, company_id")
    return render_template(
        "companies.html",
        companies=companies,
        edit_company=edit_company,
        form_values=form_values or (edit_company or {}),
        form_errors=form_errors or [],
    ), status


@app.get("/companies")
def companies_list():
    """Show all companies and the form for adding a company."""
    return _render_companies()


@app.get("/companies/<int:company_id>")
def companies_detail(company_id):
    """Show the details for one company."""
    company = fetch_one(
        "SELECT * FROM companies WHERE company_id = %s", (company_id,)
    )
    if company is None:
        abort(404)
    return render_template("company_detail.html", company=company)


@app.post("/companies")
def companies_create():
    """Create a company from the submitted form."""
    data, errors = _company_form_data()
    if errors:
        return _render_companies(form_values=data, form_errors=errors, status=400)

    insert_query(
        """INSERT INTO companies
           (company_name, industry, website, city, state, notes)
           VALUES (%s, %s, %s, %s, %s, %s)""",
        (data["company_name"], data["industry"], data["website"],
         data["city"], data["state"], data["notes"]),
    )
    flash("Company added.", "success")
    return redirect(url_for("companies_list"))


@app.route("/companies/<int:company_id>/edit", methods=["GET", "POST"])
def companies_edit(company_id):
    """Display and process the edit form for a company."""
    company = fetch_one(
        "SELECT * FROM companies WHERE company_id = %s", (company_id,)
    )
    if company is None:
        abort(404)

    if request.method == "GET":
        return _render_companies(edit_company=company)

    data, errors = _company_form_data()
    if errors:
        return _render_companies(
            edit_company=company, form_values=data, form_errors=errors, status=400
        )

    execute_query(
        """UPDATE companies
           SET company_name = %s, industry = %s, website = %s,
               city = %s, state = %s, notes = %s
           WHERE company_id = %s""",
        (data["company_name"], data["industry"], data["website"],
         data["city"], data["state"], data["notes"], company_id),
    )
    flash("Company updated.", "success")
    return redirect(url_for("companies_list"))


@app.post("/companies/<int:company_id>/delete")
def companies_delete(company_id):
    """Delete a company if no related records prevent deletion."""
    try:
        deleted_rows = execute_query(
            "DELETE FROM companies WHERE company_id = %s", (company_id,)
        )
    except IntegrityError:
        flash("This company cannot be deleted while it has related jobs or contacts.", "error")
    else:
        if deleted_rows:
            flash("Company deleted.", "success")
        else:
            flash("Company not found.", "error")

    return redirect(url_for("companies_list"))


def _job_form_data():
    """Read and validate fields submitted by the job form."""
    company_id_value = request.form.get("company_id", "").strip()
    job_type = request.form.get("job_type", "").strip() or None
    posting_url = request.form.get("posting_url", "").strip() or None
    date_posted_value = request.form.get("date_posted", "").strip()

    data = {
        "company_id": None,
        "job_title": request.form.get("job_title", "").strip(),
        "job_description": request.form.get("job_description", "").strip() or None,
        "salary_min": None,
        "salary_max": None,
        "job_type": job_type,
        "posting_url": posting_url,
        "date_posted": None,
        "is_active": request.form.get("is_active") == "on",
    }
    errors = []

    if not company_id_value.isdigit():
        errors.append("Select a company.")
    else:
        data["company_id"] = int(company_id_value)
        if fetch_one(
            "SELECT company_id FROM companies WHERE company_id = %s",
            (data["company_id"],),
        ) is None:
            errors.append("The selected company does not exist.")

    if not data["job_title"]:
        errors.append("Job title is required.")
    elif len(data["job_title"]) > 100:
        errors.append("Job title must be 100 characters or fewer.")

    if job_type and len(job_type) > 20:
        errors.append("Job type must be 20 characters or fewer.")
    if posting_url and len(posting_url) > 500:
        errors.append("Posting URL must be 500 characters or fewer.")

    max_salary = Decimal("99999999.99")
    for field, label in (("salary_min", "Minimum salary"), ("salary_max", "Maximum salary")):
        raw_value = request.form.get(field, "").strip()
        if not raw_value:
            continue
        try:
            value = Decimal(raw_value)
        except InvalidOperation:
            errors.append(f"{label} must be a valid number.")
            continue
        if not value.is_finite() or value < 0 or value > max_salary:
            errors.append(f"{label} must be between 0 and 99,999,999.99.")
            continue
        data[field] = value.quantize(Decimal("0.01"))

    if (
        data["salary_min"] is not None
        and data["salary_max"] is not None
        and data["salary_min"] > data["salary_max"]
    ):
        errors.append("Minimum salary cannot be greater than maximum salary.")

    if date_posted_value:
        try:
            data["date_posted"] = date.fromisoformat(date_posted_value)
        except ValueError:
            errors.append("Date posted must be a valid date.")

    return data, errors


def _render_jobs(edit_job=None, form_values=None, form_errors=None, status=200):
    companies = fetch_all("SELECT company_id, company_name FROM companies ORDER BY company_name")
    jobs = fetch_all(
        """SELECT j.*, c.company_name
           FROM jobs AS j
           JOIN companies AS c ON c.company_id = j.company_id
           ORDER BY j.created_at DESC, j.job_id DESC"""
    )
    if form_values is None:
        form_values = edit_job or {"is_active": True}
    return render_template(
        "jobs.html",
        jobs=jobs,
        companies=companies,
        edit_job=edit_job,
        form_values=form_values,
        form_errors=form_errors or [],
    ), status


@app.get("/jobs")
def jobs_list():
    """Show all jobs and the form for adding a job."""
    return _render_jobs()


@app.post("/jobs")
def jobs_create():
    """Create a job from the submitted form."""
    data, errors = _job_form_data()
    if errors:
        return _render_jobs(form_values=data, form_errors=errors, status=400)

    insert_query(
        """INSERT INTO jobs
           (company_id, job_title, job_description, salary_min, salary_max,
            job_type, posting_url, date_posted, is_active)
           VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
        (data["company_id"], data["job_title"], data["job_description"],
         data["salary_min"], data["salary_max"], data["job_type"],
         data["posting_url"], data["date_posted"], data["is_active"]),
    )
    flash("Job added.", "success")
    return redirect(url_for("jobs_list"))


@app.get("/jobs/<int:job_id>")
def jobs_detail(job_id):
    """Show the details for one job."""
    job = fetch_one(
        """SELECT j.*, c.company_name
           FROM jobs AS j
           JOIN companies AS c ON c.company_id = j.company_id
           WHERE j.job_id = %s""",
        (job_id,),
    )
    if job is None:
        abort(404)
    return render_template("job_detail.html", job=job)


@app.route("/jobs/<int:job_id>/edit", methods=["GET", "POST"])
def jobs_edit(job_id):
    """Display and process the edit form for a job."""
    job = fetch_one("SELECT * FROM jobs WHERE job_id = %s", (job_id,))
    if job is None:
        abort(404)

    if request.method == "GET":
        return _render_jobs(edit_job=job)

    data, errors = _job_form_data()
    if errors:
        return _render_jobs(
            edit_job=job, form_values=data, form_errors=errors, status=400
        )

    execute_query(
        """UPDATE jobs
           SET company_id = %s, job_title = %s, job_description = %s,
               salary_min = %s, salary_max = %s, job_type = %s,
               posting_url = %s, date_posted = %s, is_active = %s
           WHERE job_id = %s""",
        (data["company_id"], data["job_title"], data["job_description"],
         data["salary_min"], data["salary_max"], data["job_type"],
         data["posting_url"], data["date_posted"], data["is_active"], job_id),
    )
    flash("Job updated.", "success")
    return redirect(url_for("jobs_list"))


@app.post("/jobs/<int:job_id>/delete")
def jobs_delete(job_id):
    """Delete a job if no applications refer to it."""
    try:
        deleted_rows = execute_query(
            "DELETE FROM jobs WHERE job_id = %s", (job_id,)
        )
    except IntegrityError:
        flash("This job cannot be deleted while it has applications.", "error")
    else:
        if deleted_rows:
            flash("Job deleted.", "success")
        else:
            flash("Job not found.", "error")

    return redirect(url_for("jobs_list"))


def _contact_form_data():
    """Read and validate fields submitted by the contact form."""
    company_id_value = request.form.get("company_id", "").strip()
    data = {
        "company_id": None,
        "first_name": request.form.get("first_name", "").strip(),
        "last_name": request.form.get("last_name", "").strip(),
        "email": request.form.get("email", "").strip() or None,
        "phone": request.form.get("phone", "").strip() or None,
        "job_title": request.form.get("job_title", "").strip() or None,
        "linkedin_url": request.form.get("linkedin_url", "").strip() or None,
        "notes": request.form.get("notes", "").strip() or None,
    }
    errors = []

    if not company_id_value.isdigit():
        errors.append("Select a company.")
    else:
        data["company_id"] = int(company_id_value)
        if fetch_one(
            "SELECT company_id FROM companies WHERE company_id = %s",
            (data["company_id"],),
        ) is None:
            errors.append("The selected company does not exist.")

    for field, label in (("first_name", "First name"), ("last_name", "Last name")):
        value = data[field]
        if not value:
            errors.append(f"{label} is required.")
        elif len(value) > 50:
            errors.append(f"{label} must be 50 characters or fewer.")

    if data["email"] and len(data["email"]) > 100:
        errors.append("Email must be 100 characters or fewer.")
    if data["phone"] and len(data["phone"]) > 20:
        errors.append("Phone must be 20 characters or fewer.")
    if data["job_title"] and len(data["job_title"]) > 100:
        errors.append("Job title must be 100 characters or fewer.")
    if data["linkedin_url"] and len(data["linkedin_url"]) > 200:
        errors.append("LinkedIn URL must be 200 characters or fewer.")

    return data, errors


def _render_contacts(edit_contact=None, form_values=None, form_errors=None, status=200):
    companies = fetch_all(
        "SELECT company_id, company_name FROM companies ORDER BY company_name"
    )
    contacts = fetch_all(
        """SELECT ct.*, co.company_name
           FROM contacts AS ct
           JOIN companies AS co ON co.company_id = ct.company_id
           ORDER BY ct.last_name, ct.first_name, ct.contact_id"""
    )
    if form_values is None:
        form_values = edit_contact or {}
    return render_template(
        "contacts.html",
        contacts=contacts,
        companies=companies,
        edit_contact=edit_contact,
        form_values=form_values,
        form_errors=form_errors or [],
    ), status


@app.get("/contacts")
def contacts_list():
    """Show all contacts and the form for adding a contact."""
    return _render_contacts()


@app.post("/contacts")
def contacts_create():
    """Create a contact from the submitted form."""
    data, errors = _contact_form_data()
    if errors:
        return _render_contacts(form_values=data, form_errors=errors, status=400)

    insert_query(
        """INSERT INTO contacts
           (company_id, first_name, last_name, email, phone, job_title,
            linkedin_url, notes)
           VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
        (data["company_id"], data["first_name"], data["last_name"],
         data["email"], data["phone"], data["job_title"],
         data["linkedin_url"], data["notes"]),
    )
    flash("Contact added.", "success")
    return redirect(url_for("contacts_list"))


@app.get("/contacts/<int:contact_id>")
def contacts_detail(contact_id):
    """Show the details for one contact."""
    contact = fetch_one(
        """SELECT ct.*, co.company_name
           FROM contacts AS ct
           JOIN companies AS co ON co.company_id = ct.company_id
           WHERE ct.contact_id = %s""",
        (contact_id,),
    )
    if contact is None:
        abort(404)
    return render_template("contact_detail.html", contact=contact)


@app.route("/contacts/<int:contact_id>/edit", methods=["GET", "POST"])
def contacts_edit(contact_id):
    """Display and process the edit form for a contact."""
    contact = fetch_one(
        "SELECT * FROM contacts WHERE contact_id = %s", (contact_id,)
    )
    if contact is None:
        abort(404)

    if request.method == "GET":
        return _render_contacts(edit_contact=contact)

    data, errors = _contact_form_data()
    if errors:
        return _render_contacts(
            edit_contact=contact, form_values=data, form_errors=errors, status=400
        )

    execute_query(
        """UPDATE contacts
           SET company_id = %s, first_name = %s, last_name = %s,
               email = %s, phone = %s, job_title = %s,
               linkedin_url = %s, notes = %s
           WHERE contact_id = %s""",
        (data["company_id"], data["first_name"], data["last_name"],
         data["email"], data["phone"], data["job_title"],
         data["linkedin_url"], data["notes"], contact_id),
    )
    flash("Contact updated.", "success")
    return redirect(url_for("contacts_list"))


@app.post("/contacts/<int:contact_id>/delete")
def contacts_delete(contact_id):
    """Delete a contact."""
    deleted_rows = execute_query(
        "DELETE FROM contacts WHERE contact_id = %s", (contact_id,)
    )
    if deleted_rows:
        flash("Contact deleted.", "success")
    else:
        flash("Contact not found.", "error")
    return redirect(url_for("contacts_list"))


if __name__ == "__main__":
    app.run(debug=True)
