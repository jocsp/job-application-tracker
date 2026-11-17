# Job Application Tracker

A Flask and MySQL application for organizing companies, job listings, contacts, and applications. The dashboard summarizes job search activity, and Job Match ranks active jobs by the percentage of required skills that match your skills.

## Features

- Create, view, edit, and delete companies, jobs, contacts, and applications
- Dashboard with record totals, recent applications, and application status counts
- Job Match ranking based on exact required-skill names, ignoring capitalization and duplicate skills

## Requirements

- Python 3
- MySQL Server and the MySQL command-line client
- Git (to clone the repository)

## Setup

### 1. Clone the repository and enter the project directory

```bash
git clone https://github.com/jocsp/job-application-tracker.git
cd job-application-tracker
```

### 2. Create and activate a Python virtual environment

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install Python dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Copy the example file and edit `.env` with the connection details for your local MySQL server:

```bash
cp .env.example .env
```

Set `MYSQL_HOST`, `MYSQL_PORT`, `MYSQL_USER`, `MYSQL_PASSWORD`, and `MYSQL_DATABASE`. Generate a Flask secret key with:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Put the generated value in `FLASK_SECRET_KEY` in `.env`. The `.env` file is ignored by Git; do not commit your local credentials.

### 5. Create or update the MySQL database

For a **new database**, run the schema from the project directory:

```bash
mysql -u root -p < schema.sql
```

Replace `root` with your MySQL user if needed. `schema.sql` creates and selects the `job_tracker` database and creates its tables.

For an **existing `job_tracker` database**, apply the required-skills migration once:

```bash
mysql -u root -p < migration_add_required_skills.sql
```

This adds the `required_skills` column used by Job Match. Don’t run this migration again after the column has been added.

Optional: load sample records into a newly created, empty database:

```bash
mysql -u root -p < seed.sql
```

`seed.sql` inserts sample companies, jobs, applications, and contacts. Run it only once against an empty database to avoid duplicate records or incorrect sample relationships.

### 6. Start the Flask application

With the virtual environment active and MySQL running:

```bash
python app.py
```

Open <http://127.0.0.1:5000> in your browser. The root page is the dashboard. Use **Jobs** to add job requirements and **Job Match** to enter your own skills and compare them.

## Job Match

Enter required skills on each job record and your skills on the Job Match page. Separate skills with commas or put one skill on each line. Each score is calculated as:

```text
number of matched required skills / number of required skills * 100
```

Jobs are ranked by that percentage. Active jobs with no required skills remain listed without a score. Your entered skill list is kept in the Flask session.

## Technologies

- Python and Flask
- MySQL with `mysql-connector-python`
- HTML and CSS
- `python-dotenv` for local environment variables
