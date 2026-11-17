# Job Application Tracker

A web application to help track job applications during the job search process.

## Features
- Track companies, job listings, contacts, and applications
- View job search totals and recent application activity on the dashboard
- Rank active jobs by the percentage of required skills matching your skills

## Job Match setup
Add required skills to each job as comma-separated values or one skill per line. Open **Job Match**, enter your skills in the same format, and the page ranks active jobs by the exact skill-name matches. Matching ignores capitalization and duplicate entries.

For an existing database, run [`migration_add_required_skills.sql`](migration_add_required_skills.sql) once before starting the updated app. New databases created from `schema.sql` include this field already.

## Technologies
- MySQL Database
- Python with Flask
- HTML/CSS for the web interface
