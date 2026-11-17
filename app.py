"""Initial Flask application for the Job Application Tracker."""

import os

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


if __name__ == "__main__":
    app.run(debug=True)
