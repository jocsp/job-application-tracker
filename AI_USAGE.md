# AI Usage Documentation

## Tools Used

- Codex (GPT-6): reviewed repository changes, suggested a commit message, and initialized this usage log.
  Also generated the initial MySQL schema and reviewed it against the requested fields and relationships.

## Key Prompts

- "which should be the commit message for the changes currently done"
- Requested a root-level `schema.sql` defining companies, jobs, applications, and contacts with the supplied columns, types, and foreign keys.
- Asked what `schema.sql` is for and whether it creates the database from scratch.
- Asked whether the project should include a script that inserts dummy data.
- Asked whether `database.py` and `app.py` are the two backend files for a Python/Flask CRUD implementation.
- Asked which of the two backend files makes sense to create first.
- Asked for a step-by-step plan for implementing the Python/Flask backend and CRUD operations.
- Asked to create `database.py` with a simple MySQL connection and helpers.
- Asked how to create the MySQL environment variables used by `database.py`.
- Asked whether the MySQL environment variables can be stored in a `.env` file as in Node/Express.
- Asked to create both `.env` and `.env.example` and add `python-dotenv` to `requirements.txt`.
- Asked for a project status review and a step-by-step plan to finish the application.
- Asked for a commit message for the current backend and environment configuration changes.
- Asked to fix `seed.sql` so it matches the database schema and provide a commit message.
- Asked to create the initial `app.py`, test the database connection with the provided environment variables, and suggest a commit message.
- Asked to implement company CRUD operations in the Flask project and provide commit messages.
- Asked to implement CRUD operations for jobs and provide a commit message.
- Asked to add CRUD operations for contacts.
- Asked whether a proposed alternate schema is the same as or has a similar outcome to `schema.sql`.
- Asked to add the fields from the alternate schema to `schema.sql`.
- Asked whether the updated `schema.sql` now exactly matches the provided alternate schema.
- Asked to make `schema.sql` match the newly supplied schema exactly.
- Asked to add a dashboard and a job matching feature that ranks jobs by the percentage of required skills matching the user's skills, and requested a commit message.
- Asked to update the README with setup instructions.
- Asked to replace the page-shifting success message with a toast notification that disappears after about five seconds.

## What Worked Well

- Repository inspection identified two untracked documentation files and no tracked changes, supporting a documentation-focused commit message.
- The dashboard can summarize existing application data, and the matching feature uses explicitly entered skill lists so it can calculate transparent exact-skill percentages.
- The README setup steps reflect the repository's current requirements, environment template, fresh-install schema, existing-database migration, and optional seed script.
- Success notices now use a fixed toast overlay, so they don’t push page content down; error notices remain visible until dismissed.

## What I Modified

- The AI assistant populated the previously empty `AI_USAGE.md`. Independent student modifications have not been documented or confirmed.
- The AI assistant created `schema.sql` from the user-provided schema; no independent student edits to that output are confirmed.
- The AI assistant added a nullable `required_skills` field and an upgrade script because the existing jobs schema did not store the skill list needed for matching. The user's skill list is held in the Flask session; no independent student modifications to this work are confirmed.
- The AI assistant rewrote `README.md` with installation and run instructions; no independent student modifications are confirmed.
- The AI assistant changed the shared flash-message presentation to fixed toast notifications; no independent student modifications are confirmed.

## Lessons Learned

- Pending student reflection.

## Detailed AI Usage Log

### 2026-11-15 — Review changes and suggest a commit message

**AI Tool:** Codex (GPT-6)

**Purpose:** Suggest a commit message matching the current repository changes.

**Key Prompt(s):**
- "which should be the commit message for the changes currently done"

**AI Contribution:**
- Inspected Git status, staged and unstaged diff summaries, recent commit messages, and project AI instructions.
- Suggested `docs: add AI instructions and usage documentation`.
- Initialized this documentation with the required sections and a factual task entry.

**Changes and Modifications:**
- AI populated the empty `AI_USAGE.md`; no application code was changed.
- Student modifications have not been documented or confirmed.

**Files Affected:**
- `AGENTS.md` (reviewed).
- `AI_USAGE.md` (reviewed and populated).

**Testing and Verification:**
- Ran `git status --short`, `git diff --stat`, and `git diff --cached --stat`: only `AGENTS.md` and `AI_USAGE.md` were untracked; no tracked diffs appeared.
- Ran `git log -4 --oneline`, read both documentation files, and confirmed `AI_USAGE.md` was initially empty with `ls -l`.
- No tests were executed; this task involved documentation only. No commit was created.

**What Worked Well:**
- Inspection established that the pending changes concern AI project instructions and usage documentation.

**Lessons Learned:**
- Pending student reflection.
### 2026-11-17 — Implement company CRUD pages and routes

**AI Tool:** Codex (GPT-6 Thinking)

**Purpose:** Add company create, read, update, and delete functionality to the Flask application.

**Key Prompt(s):**
- "there is already a job_tracker database in mysql, let's now create crud operations for the companies and give me the commit messages"

**AI Contribution:**
- Inspected the live `companies` table columns using a read-only `SHOW COLUMNS` query; it includes the planned fields and an additional nullable `created_at` column.
- Added routes to list, view, create, edit, and delete company records, plus form validation and foreign-key deletion feedback.
- Added the shared page layout, companies list/form, company detail page, and responsive CSS.
- Used parameterized queries through `database.py` helpers.

**Changes and Modifications:**
- AI modified `app.py` and `static/style.css`, created `templates/base.html`, `templates/companies.html`, and `templates/company_detail.html`, and updated this log. No student modifications are confirmed.

**Files Affected:**
- `app.py` (modified).
- `templates/base.html` (created).
- `templates/companies.html` (created).
- `templates/company_detail.html` (created).
- `static/style.css` (created).
- `AI_USAGE.md` (reviewed and updated).
- MySQL `companies` table metadata (read only).

**Testing and Verification:**
- Read the actual `companies` table column metadata through the configured database connection.
- No CRUD writes or application tests were run; no company data was changed.

**What Worked Well:**
- The route queries use the live table's column names and allow its extra nullable `created_at` field without requiring schema changes.

**Lessons Learned:**
- Pending student reflection.
### 2026-11-17 — Create initial Flask app and verify database connection

**AI Tool:** Codex (GPT-6 Thinking)

**Purpose:** Create the first Flask application file and check connectivity using local environment settings.

**Key Prompt(s):**
- "create the initial app.py and test whether we can connect to the database using the env variables that i just provided"
- "and give me the commit message"

**AI Contribution:**
- Created `app.py` with a basic home route and `/health/database` route.
- Ran a direct `SELECT 1` through `database.py`, then requested the Flask database health route through Flask's test client.
- Recommended `feat: add initial Flask app and database health check`.

**Changes and Modifications:**
- AI created `app.py` and updated this log. No student modifications are confirmed.

**Files Affected:**
- `app.py` (created).
- `AI_USAGE.md` (reviewed and updated).
- `.env` and `database.py` (used for verification).

**Testing and Verification:**
- Using the project's `.venv`, the direct `SELECT 1 AS connected` query passed.
- Flask's `/health/database` test-client request returned HTTP 200 with `{"database":"connected"}`.
- No other application tests were run.

**What Worked Well:**
- Both the database helper and the Flask health route connected successfully using the local `.env` configuration.

**Lessons Learned:**
- Pending student reflection.

### 2026-11-17 — Align seed data with the database schema

**AI Tool:** Codex (GPT-6 Thinking)

**Purpose:** Correct the sample data script so its inserts and status updates conform to the current table definitions.

**Key Prompt(s):**
- "fix seed.sql and give me the commit message"

**AI Contribution:**
- Changed contact inserts to use the schema's `contact_name` and `title` columns.
- Replaced unsupported application statuses with allowed enum values: `Screening`, `Interview`, and `Offer`.

**Changes and Modifications:**
- AI edited `seed.sql` and updated this log. No student modifications are confirmed.

**Files Affected:**
- `seed.sql` (modified and reviewed).
- `AI_USAGE.md` (reviewed and updated).
- `schema.sql` (reviewed for compatibility).

**Testing and Verification:**
- Compared all changed status values and contact column names with `schema.sql`.
- Ran `git diff --check`; it reported no whitespace errors.
- Did not execute the script against MySQL, so runtime behavior remains unverified.

**What Worked Well:**
- The modified contact fields and application statuses now match the names and enum values in `schema.sql` by inspection.

**Lessons Learned:**
- Pending student reflection.

### 2026-11-17 — Review project progress and remaining work

**AI Tool:** Codex (GPT-6 Thinking)

**Purpose:** Compare the current repository with the course specification and identify completed work, gaps, and a practical order to continue.

**Key Prompt(s):**
- "it's been a while since I worked in this project, let me know what remains to do, what parts have we done so far and what parts are missing, which is a plan to continue doing the rest."

**AI Contribution:**
- Inspected tracked files, recent commits, the schema, seed script, database helper module, requirements, and README.
- Read the course project specification and identified the required CRUD pages, dashboard, job matching feature, setup documentation, and recorded demo.
- Compared `seed.sql` statements with the current schema and found incompatible application status values and contact column names.

**Changes and Modifications:**
- No application code was changed. This log was updated to record the review.

**Files Affected:**
- `AI_USAGE.md` (reviewed and updated).
- `README.md`, `requirements.txt`, `database.py`, `schema.sql`, `seed.sql`, and files under `specifications/` (reviewed).

**Testing and Verification:**
- Ran `git status --short`, `git log -6 --oneline`, and listed repository files.
- Extracted and reviewed the project requirements from the DOCX specification.
- No application tests or database execution were performed.

**What Worked Well:**
- The file and specification review provided a concrete baseline and exposed that the current seed data does not match the schema.

**Lessons Learned:**
- Pending student reflection.

### 2026-11-16 — Suggest a commit message for backend setup

**AI Tool:** Codex (GPT-6 Luna)

**Purpose:** Suggest a commit message based on the current staged and unstaged changes.

**Key Prompt(s):**
- "give me the commit message for these changes"

**AI Contribution:**
- Reviewed Git status and change summaries to identify the MySQL helper module, dotenv support, dependency update, and example configuration file.
- Recommended `feat: add MySQL connection helpers and dotenv config`.

**Changes and Modifications:**
- No application source changes were made for this request. This usage log was updated.

**Files Affected:**
- `AI_USAGE.md` (reviewed and updated).
- Git status and diff summaries (reviewed).

**Testing and Verification:**
- Ran `git status --short` and staged/unstaged `git diff --stat` summaries.
- No tests were run; this was commit-message guidance.

**What Worked Well:**
- The suggested message reflects the backend database connection helpers and environment-based configuration.

**Lessons Learned:**
- Pending student reflection.

### 2026-11-16 — Add `.env` support for MySQL settings

**AI Tool:** Codex (GPT-6 Luna)

**Purpose:** Let the Python backend load local MySQL connection settings from a `.env` file.

**Key Prompt(s):**
- "can it be done with an .env file like with node and express?"

**AI Contribution:**
- Added `python-dotenv` to `requirements.txt` and configured `database.py` to load the project-root `.env` file.
- Added `.env.example` with the expected MySQL variable names and placeholder values.
- Confirmed the existing `.gitignore` already ignores `.env`, keeping local credentials out of Git.

**Changes and Modifications:**
- AI modified `database.py`, `requirements.txt`, and `AI_USAGE.md`, and created `.env.example`.
- No actual `.env` file or credentials were created.

**Files Affected:**
- `database.py` (modified).
- `requirements.txt` (modified).
- `.env.example` (created).
- `.gitignore` (reviewed; already ignores `.env`).
- `AI_USAGE.md` (reviewed and updated).

**Testing and Verification:**
- Reviewed the changes and verified `.env` is listed in the existing `.gitignore`.
- No package installation, application run, or database connection test was performed.

**What Worked Well:**
- The sample environment file documents configuration without storing actual secrets in the repository.

**Lessons Learned:**
- Python needs `python-dotenv` and an explicit `load_dotenv()` call for this module to read `.env` values when the app starts.

### 2026-11-16 — Create local and example environment files

**AI Tool:** Codex (GPT-6 Luna)

**Purpose:** Provide both a local environment file and a shareable example for MySQL settings.

**Key Prompt(s):**
- "let's create a .env and a .env.example, also include python-dotenv in the requirements.txt"

**AI Contribution:**
- Created `.env` with local MySQL settings and an empty password value for the user to fill in.
- Kept `.env.example` with a placeholder password for others to copy and customize.
- Verified the existing `.gitignore` excludes `.env`.

**Changes and Modifications:**
- Created `.env`; `.env.example`, `requirements.txt`, and `database.py` had already been updated to support this configuration in the preceding step.
- No real database password was provided or added.

**Files Affected:**
- `.env` (created; ignored by Git).
- `.env.example` (reviewed).
- `requirements.txt` (reviewed).
- `database.py` (reviewed).
- `AI_USAGE.md` (reviewed and updated).

**Testing and Verification:**
- Ran `git check-ignore .env`; Git confirmed `.env` is ignored.
- No application or database tests were run.

**What Worked Well:**
- The local file is ready for the user to add their local password while the example remains safe to share.

**Lessons Learned:**
- Pending student reflection.

### 2026-11-16 — Explain how to set MySQL environment variables

**AI Tool:** Codex (GPT-6 Luna)

**Purpose:** Explain how to provide local MySQL settings to the connection helper on macOS zsh.

**Key Prompt(s):**
- "how do i create the environment variables?"

**AI Contribution:**
- Explained temporary `export` commands for the current terminal session and persistent shell configuration as an option.
- Clarified that the Flask process must be started from the shell where the variables are set, and that the current code does not automatically load a `.env` file.

**Changes and Modifications:**
- No environment variables or source files were changed. This usage log was updated.

**Files Affected:**
- `AI_USAGE.md` (reviewed and updated).
- `database.py` (reviewed as context).

**Testing and Verification:**
- No commands were run and no environment values were set; this was usage guidance.

**What Worked Well:**
- The explanation distinguishes session-only variables from persistent shell configuration.

**Lessons Learned:**
- Pending student reflection.

### 2026-11-16 — Recommend backend implementation order

**AI Tool:** Codex (GPT-6 Luna)

**Purpose:** Recommend which planned Flask backend module to create first.

**Key Prompt(s):**
- "which one it makes sense to create first?"

**AI Contribution:**
- Recommended creating `database.py` first to establish the MySQL connection interface that `app.py` will import and use for CRUD routes.

**Changes and Modifications:**
- No backend code was created or changed. This usage log was updated.

**Files Affected:**
- `AI_USAGE.md` (reviewed and updated).

**Testing and Verification:**
- No tests or commands were run; this was sequencing guidance.

**What Worked Well:**
- The suggested order follows the dependency between the database helper module and Flask routes.

**Lessons Learned:**
- Pending student reflection.

### 2026-11-16 — Create MySQL connection helpers

**AI Tool:** Codex (GPT-6 Luna)

**Purpose:** Create the first backend module for connecting to MySQL and supporting CRUD queries.

**Key Prompt(s):**
- "let's create the database.py file with a simple connection and simple helpers"

**AI Contribution:**
- Created `database.py` with `get_db_connection()` using environment variables for MySQL settings and local development defaults.
- Added `fetch_all()` and `fetch_one()` for SELECT queries, `insert_query()` to return the inserted row ID, and `execute_query()` to return affected row counts for updates/deletes.
- Added commit on successful writes, rollback on write errors, and cursor/connection cleanup.

**Changes and Modifications:**
- AI created `database.py` and updated this log. No student modifications are confirmed.
- No changes were made to `requirements.txt`; it already lists `mysql-connector-python`.

**Files Affected:**
- `database.py` (created).
- `AI_USAGE.md` (reviewed and updated).
- `requirements.txt` (reviewed).

**Testing and Verification:**
- Reviewed the implementation against the requested connection and helper responsibilities.
- No tests or runtime database connection were executed.

**What Worked Well:**
- The helpers use parameterized query arguments, return dictionaries for reads, and close resources after each call.

**Lessons Learned:**
- Pending student reflection.

### 2026-11-16 — Plan the Flask backend CRUD implementation

**AI Tool:** Codex (GPT-6 Luna)

**Purpose:** Provide an implementation sequence for the planned Flask and MySQL backend.

**Key Prompt(s):**
- "give me a plan for the changes we have to do for the backend, step by step"

**AI Contribution:**
- Proposed a dependency-ordered plan: database connectivity, shared database helpers, Flask app setup, then CRUD for companies, jobs and contacts, and applications.
- Included related implementation considerations for form routes, validation, foreign keys, JSON fields, and database errors.

**Changes and Modifications:**
- No backend source files were created or modified. This usage log was updated.

**Files Affected:**
- `AI_USAGE.md` (reviewed and updated).
- `schema.sql` and repository file listing (reviewed as context).

**Testing and Verification:**
- Read the current AI usage log and listed repository files; no `app.py` or `database.py` exists yet.
- No tests or commands were run for application code; this was planning guidance.

**What Worked Well:**
- The plan can follow the database relationships, implementing parent records before dependent records.

**Lessons Learned:**
- Pending student reflection.

### 2026-11-15 — Create the initial MySQL schema

**AI Tool:** Codex (GPT-6)

**Purpose:** Start the requested project structure with the database creation script.

**Key Prompt(s):**
- "let's start by creating the schemas for the next" followed by the complete companies, jobs, applications, and contacts field definitions and the desired project structure.

**AI Contribution:**
- Created root-level `schema.sql` to create and select the `job_tracker` database using utf8mb4.
- Defined all four tables with the requested auto-increment primary keys, column types, ENUM values, JSON fields, and NOT NULL declarations.
- Added the three requested foreign keys and used InnoDB for foreign key enforcement.
- Kept unspecified fields nullable and used default restrictive foreign key behavior; no cascading deletion was added.

**Changes and Modifications:**
- AI generated the schema and updated this log. No student modifications to the generated output are confirmed.
- Other proposed application files were not created because this task starts with the schema.

**Files Affected:**
- `schema.sql` (created and reviewed).
- `AI_USAGE.md` (reviewed and updated).
- `README.md` and `requirements.txt` (reviewed).

**Testing and Verification:**
- Inspected repository file listings and `git status --short` before editing.
- Read back the generated SQL and reviewed its fields and foreign key targets against the request.
- Ran `git diff --check` with no reported errors; this does not validate untracked SQL or MySQL execution.
- Checked for `mysql` and `mariadb`; neither client was available on PATH. Docker was present, but no database instance was started.
- No database execution tests were run. The table creation statements are intended for initial setup and will fail if those tables already exist.

**What Worked Well:**
- The generated script includes the requested four tables and three relationships in dependency order, as confirmed by review.
- Runtime correctness has not yet been verified against MySQL.

**Lessons Learned:**
- Pending student reflection.

### 2026-11-15 — Explain the purpose of `schema.sql`

**AI Tool:** Codex (GPT-6 Luna)

**Purpose:** Explain what the database schema script creates and distinguish structure from application records.

**Key Prompt(s):**
- "in this context, what is the schema.sql file for? to create the database from scratch with all the information?"

**AI Contribution:**
- Explained that the script creates the `job_tracker` database and the four table definitions, including columns, types, keys, and relationships.
- Clarified that it creates an empty database structure, not sample or actual company, job, application, or contact records.

**Changes and Modifications:**
- No SQL changes were made. This usage log was updated to record the explanation.

**Files Affected:**
- `schema.sql` (reviewed).
- `AI_USAGE.md` (reviewed and updated).

**Testing and Verification:**
- Read `schema.sql` to confirm it creates/selects `job_tracker` and defines four tables.
- No commands or database tests were run.

**What Worked Well:**
- The distinction between creating the schema and populating it with records directly answers what the script does.

**Lessons Learned:**
- Pending student reflection.

### 2026-11-15 — Recommend how to manage sample database records

**AI Tool:** Codex (GPT-6 Luna)

**Purpose:** Advise whether to include dummy data alongside the initial database schema.

**Key Prompt(s):**
- "should I also make the script to create the database with some dummy data? or not?"

**AI Contribution:**
- Recommended keeping table definitions in `schema.sql` and putting optional development/demo records in a separate seed script, such as `seed.sql`.
- Explained that sample records are useful for testing and demonstrations, while separate scripts let the project be initialized with an empty database when needed.

**Changes and Modifications:**
- No project files besides this usage log were changed; no seed script was created.

**Files Affected:**
- `AI_USAGE.md` (reviewed and updated).

**Testing and Verification:**
- No tests or commands were run; this was design guidance only.

**What Worked Well:**
- The recommendation separates database structure from optional sample content.

**Lessons Learned:**
- Pending student reflection.

### 2026-11-16 — Explain the roles of the Flask backend files

**AI Tool:** Codex (GPT-6 Luna)

**Purpose:** Clarify whether `app.py` and `database.py` are the backend files for the planned CRUD features.

**Key Prompt(s):**
- "I want to start first with the backend with python and flask. I want to do the crud operations for each table. I understand that the backend is present in these two files right database.py app.py"

**AI Contribution:**
- Confirmed that these are a sensible two-file starting structure: `app.py` holds Flask routes and CRUD request handling; `database.py` centralizes MySQL connection and database helper functions.
- Noted that server-rendered HTML templates are presentation files, while a larger project can later split routes or services into additional modules.
- Checked the repository file list and found that `app.py` and `database.py` do not exist yet; they are part of the proposed structure, not implemented files at this point.

**Changes and Modifications:**
- No backend files were created or modified. This usage log was updated.

**Files Affected:**
- `AI_USAGE.md` (reviewed and updated).
- Repository file listing (reviewed).

**Testing and Verification:**
- Ran `rg --files`; the repository currently lists `schema.sql`, `seed.sql`, `AGENTS.md`, `requirements.txt`, `README.md`, and `AI_USAGE.md`, with no `app.py` or `database.py`.
- No tests were run; this was architectural guidance only.

**What Worked Well:**
- Repository inspection distinguished the intended layout from files that have actually been created.

**Lessons Learned:**
- Pending student reflection.

### 2026-11-17 — Implement company CRUD functionality

**AI Tool:** Codex (GPT-6 Thinking)

**Purpose:** Implement create, read, update, and delete for company records in the Flask application.

**Key Prompt(s):**
- "there is already a job_tracker database in mysql, let's now create crud operations for the companies and give me the commit messages"

**AI Contribution:**
- Inspected the live `companies` table with a read-only `SHOW COLUMNS` query; it has the planned columns plus a nullable `created_at` field.
- Added list, detail, create, edit, and delete routes using parameterized SQL and the existing database helpers.
- Added required-field and length validation, confirmation before deletion, and a message when related jobs or contacts block deletion.
- Created shared layout, companies list/form and detail templates, plus responsive styling. Added a development secret key fallback so Flask flash messages work; `.env.example` shows how to configure `FLASK_SECRET_KEY`.
- Suggested commit message `feat: add CRUD operations for companies`.

**Changes and Modifications:**
- AI modified `app.py`, `.env.example`, and `static/style.css`; created `templates/base.html`, `templates/companies.html`, and `templates/company_detail.html`; updated this log. No student modifications are confirmed.

**Files Affected:**
- `app.py` (modified).
- `.env.example` (modified).
- `static/style.css` (created and modified).
- `templates/base.html` (created).
- `templates/companies.html` (created).
- `templates/company_detail.html` (created).
- `AI_USAGE.md` (reviewed and updated).
- MySQL `companies` table metadata (read only).

**Testing and Verification:**
- Confirmed the live table's column names through a read-only query.
- Ran `git diff --check`; it reported no whitespace errors.
- Did not run CRUD tests or alter company data.

**What Worked Well:**
- The routes match the existing table fields and accommodate its extra nullable `created_at` column.

**Lessons Learned:**
- Pending student reflection.

### 2026-11-17 — Compare an alternate schema with `schema.sql`

**AI Tool:** Codex (GPT-6 Thinking)

**Purpose:** Explain structural similarities and differences between the user's proposed MySQL schema and the repository schema.

**Key Prompt(s):**
- Asked whether the provided schema has the same or a similar outcome as the current `schema.sql`.

**AI Contribution:**
- Compared the four tables' columns, types, nullability, defaults, constraints, JSON fields, timestamps, and indexes.
- Noted that the repository's database schema and the live companies table differ by at least the `created_at` column.

**Changes and Modifications:**
- No application or SQL files were changed. This usage log was updated.

**Files Affected:**
- `schema.sql` and `AI_USAGE.md` (reviewed; log updated).

**Testing and Verification:**
- Read `schema.sql` and compared it with the schema supplied in the prompt.
- No database changes or tests were run.

**What Worked Well:**
- A side-by-side comparison identifies which design choices affect compatibility and stored data.

**Lessons Learned:**
- Pending student reflection.

### 2026-11-17 — Add the alternate schema's fields

**AI Tool:** Codex (GPT-6 Thinking)

**Purpose:** Extend the repository schema with fields from the user's alternate schema while retaining existing columns.

**Key Prompt(s):**
- "modify the schema.sql to add these new fields"

**AI Contribution:**
- Added timestamps to all four tables; job description, posting URL, active flag; application response/interview dates and notes; and contact first name, last name, and job title.
- Added the four indexes from the alternate schema.
- Updated seed contact inserts to supply the newly required first and last name fields.

**Changes and Modifications:**
- AI modified `schema.sql`, `seed.sql`, and this log. Existing columns and their types were retained, so some concepts now have parallel fields (for example, `job_url` and `posting_url`). No student modifications are confirmed.

**Files Affected:**
- `schema.sql` (modified).
- `seed.sql` (modified for required contact fields).
- `AI_USAGE.md` (reviewed and updated).

**Testing and Verification:**
- Reviewed the SQL diff and ran `git diff --check` with no whitespace errors.
- Did not run the schema against MySQL because the database already exists and the script uses `CREATE TABLE` statements rather than `ALTER TABLE` migrations.

**What Worked Well:**
- The seed contact inserts now provide values for the new required name columns.

**Lessons Learned:**
- Before implementing jobs and contacts CRUD, choose which of the parallel URL, title, and name fields the application will use.

### 2026-11-17 — Confirm schema alignment

**AI Tool:** Codex (GPT-6 Thinking)

**Purpose:** Check whether the expanded project schema exactly matches the user's supplied schema.

**Key Prompt(s):**
- Asked whether the modified `schema.sql` now matches the supplied version.

**AI Contribution:**
- Compared the current SQL definitions for nullability, data types, defaults, and extra columns.
- Clarified that the schema is not an exact match and identified the remaining differences.

**Changes and Modifications:**
- No schema changes were made. This usage log was updated.

**Files Affected:**
- `schema.sql` and `AI_USAGE.md` (reviewed; log updated).

**Testing and Verification:**
- Read `schema.sql` and compared it with the schema in the prompt. No database operation or tests were run.

**What Worked Well:**
- The comparison identified incompatible constraints and duplicate columns that should be resolved before implementing related CRUD features.

**Lessons Learned:**
- Pending student reflection.

### 2026-11-17 — Make `schema.sql` match the supplied schema

**AI Tool:** Codex (GPT-6 Thinking)

**Purpose:** Replace the project's schema definitions with the exact table columns, constraints, defaults, and indexes in the user's supplied schema.

**Key Prompt(s):**
- "make schema.sql match the new schema i'm passing to you"

**AI Contribution:**
- Replaced `schema.sql` definitions to match the supplied four-table schema, including nullability, decimal salary types, string status/job types, defaults, timestamps, and indexes.
- Updated contact inserts in `seed.sql` to use the new first/last name and job-title columns.

**Changes and Modifications:**
- AI modified `schema.sql`, `seed.sql`, and this log. No student modifications are confirmed.
- The existing MySQL database was not altered.

**Files Affected:**
- `schema.sql` (replaced with requested schema).
- `seed.sql` (updated to match contact columns).
- `AI_USAGE.md` (reviewed and updated).

**Testing and Verification:**
- Reviewed the SQL changes and ran `git diff --check`.
- Did not execute the schema or seed script; the user has an existing database and this setup script uses `CREATE TABLE` statements.

**What Worked Well:**
- The schema and seed contact inserts now use the same field names.

**Lessons Learned:**
- Pending student reflection.

### 2026-11-17 — Review company CRUD against the updated schema

**AI Tool:** Codex (GPT-6 Thinking)

**Purpose:** Determine whether company CRUD routes and forms need changes after the schema update.

**Key Prompt(s):**
- "see if the crud operations for the companies need updating based on the new schema"

**AI Contribution:**
- Compared the company form fields and CRUD SQL with the updated `companies` definition.
- Read the live `companies` table metadata using `SHOW COLUMNS` and confirmed it has the same columns, including `created_at` with a current-timestamp default.
- Determined that inserts may omit `created_at` because MySQL supplies the default; reads and updates remain compatible.

**Changes and Modifications:**
- No application files were changed. This usage log was updated.

**Files Affected:**
- `app.py`, `templates/companies.html`, `templates/company_detail.html`, `schema.sql`, and `AI_USAGE.md` (reviewed; log updated).
- Live MySQL `companies` table metadata (read only).

**Testing and Verification:**
- Ran a read-only `SHOW COLUMNS FROM companies` query through the configured database connection.
- No CRUD writes or application tests were run.

**What Worked Well:**
- The actual table metadata confirms the current company CRUD field names and defaults remain compatible.

**Lessons Learned:**
- Pending student reflection.

### 2026-11-17 — Implement job CRUD pages and routes

**AI Tool:** Codex (GPT-6 Thinking)

**Purpose:** Add create, read, update, and delete functionality for jobs using the current MySQL schema.

**Key Prompt(s):**
- "let continue with the crud operations for jobs and give me the commit message"

**AI Contribution:**
- Read the live `jobs` and `companies` column metadata and confirmed the job table matches the updated schema.
- Added routes to list, view, create, edit, and delete jobs, including company relationship validation, decimal salary and date validation, and deletion feedback when applications reference a job.
- Added the jobs form/list page, job detail page, navigation link, and styling.
- Suggested commit message `feat: add CRUD operations for jobs`.

**Changes and Modifications:**
- AI modified `app.py`, `templates/base.html`, and `static/style.css`; created `templates/jobs.html` and `templates/job_detail.html`; updated this log. No student modifications are confirmed.

**Files Affected:**
- `app.py` (modified).
- `templates/base.html` (modified).
- `templates/jobs.html` (created).
- `templates/job_detail.html` (created).
- `static/style.css` (modified).
- `AI_USAGE.md` (reviewed and updated).
- Live MySQL `jobs` and `companies` table metadata (read only).

**Testing and Verification:**
- Ran read-only `SHOW COLUMNS` queries for `jobs` and `companies`.
- Ran `git diff --check`; no whitespace errors were reported.
- Did not run CRUD operations or change job records.

**What Worked Well:**
- The SQL field names and types correspond to the live `jobs` table, and the company dropdown is based on live company records.

**Lessons Learned:**
- Pending student reflection.

### 2026-11-17 — Implement contact CRUD pages and routes

**AI Tool:** Codex (GPT-6 Thinking)

**Purpose:** Add create, read, update, and delete functionality for contact records.

**Key Prompt(s):**
- "let's add crud operations for contacts"

**AI Contribution:**
- Inspected live `contacts` and `companies` table columns using read-only metadata queries.
- Added contact list, detail, create, edit, and delete routes with company relationship validation and field length validation.
- Added a contact form/list page, contact detail page, navigation link, and responsive layout styling.
- Contact deletion removes only the contact record; it does not delete the associated company.

**Changes and Modifications:**
- AI modified `app.py`, `templates/base.html`, and `static/style.css`; created `templates/contacts.html` and `templates/contact_detail.html`; updated this log. No student modifications are confirmed.

**Files Affected:**
- `app.py` (modified).
- `templates/base.html` (modified).
- `templates/contacts.html` (created).
- `templates/contact_detail.html` (created).
- `static/style.css` (modified).
- `AI_USAGE.md` (reviewed and updated).
- Live MySQL `contacts` and `companies` table metadata (read only).

**Testing and Verification:**
- Ran read-only `SHOW COLUMNS` queries for `contacts` and `companies`.
- Ran `git diff --check`; no whitespace errors were reported.
- Did not run CRUD operations or change contact records.

**What Worked Well:**
- The form and SQL fields match the live contact table's separate first and last names and company foreign key.

**Lessons Learned:**
- Pending student reflection.

### 2026-11-17 — Implement application CRUD pages and routes

**AI Tool:** Codex (GPT-6 Thinking)

**Purpose:** Add create, read, update, and delete functionality for application records.

**Key Prompt(s):**
- "let's add crud operations for applications"

**AI Contribution:**
- Inspected live `applications` and `jobs` table columns through read-only metadata queries.
- Added application list, detail, create, edit, and delete routes; forms validate the selected job, required application date, optional response/interview dates, status length, and resume version length.
- Added the applications form/list page, detail page, navigation link, and responsive styling.

**Changes and Modifications:**
- AI modified `app.py`, `templates/base.html`, and `static/style.css`; created `templates/applications.html` and `templates/application_detail.html`; updated this log. No student modifications are confirmed.

**Files Affected:**
- `app.py` (modified).
- `templates/base.html` (modified).
- `templates/applications.html` (created).
- `templates/application_detail.html` (created).
- `static/style.css` (modified).
- `AI_USAGE.md` (reviewed and updated).
- Live MySQL `applications` and `jobs` table metadata (read only).

**Testing and Verification:**
- Ran read-only `SHOW COLUMNS` queries for `applications` and `jobs`.
- Ran `git diff --check`; no whitespace errors were reported.
- Did not run CRUD operations or change application records.

**What Worked Well:**
- The query and form fields match the live application table, and the job selector uses existing job and company names.

**Lessons Learned:**
- Pending student reflection.

### 2026-11-17 — Review CRUD forms and strengthen validation

**AI Tool:** Codex (GPT-6 Thinking)

**Purpose:** Ensure the CRUD pages provide listing, adding, editing, and deleting flows for each table, with server-side validation and clear foreign-key error handling.

**Key Prompt(s):**
- "please build the templates and forms for listing, adding, editing, and deleting records, also add input validation and handle foreign key errors such as trying to delete a company that still has jobs or contacts."

**AI Contribution:**
- Reviewed the existing list, detail, add, edit, and delete flows for companies, jobs, contacts, and applications.
- Added server-side URL validation for company websites, job postings, and LinkedIn profiles, plus basic email format validation for contacts.
- Added friendly handling for database constraint errors during create/update operations when a related company or job is removed before the form is saved. Existing delete handlers already report when a company has jobs or contacts, or a job has applications.

**Changes and Modifications:**
- AI modified `app.py` and this log. The CRUD templates and forms were already present from the earlier table-specific CRUD work and were reviewed without modification. No student modifications are confirmed.

**Files Affected:**
- `app.py` (modified).
- `AI_USAGE.md` (updated).
- Existing CRUD templates (reviewed; unchanged).

**Testing and Verification:**
- Ran `git diff --check`; no whitespace errors were reported.
- Did not run the Flask application or exercise CRUD operations against MySQL.

**What Worked Well:**
- Validation runs on the server as well as in the browser, and foreign-key failures return a useful message instead of an unhandled database error.

**Lessons Learned:**
- Pending student reflection.

### 2026-11-17 — Add dashboard and job skill matching

**AI Tool:** Codex (GPT-6 Thinking)

**Purpose:** Add a dashboard summarizing job search activity and a page that ranks active jobs by the percentage of required skills matching the user's skills.

**Key Prompt(s):**
- "Add the dashboard and the job match feature, which should rank jobs by the percentage of required skills that match the user’s skills."
- "and give me the commit message."

**AI Contribution:**
- Replaced the root JSON placeholder with a dashboard showing record totals, recent applications, and application status counts.
- Added required skills to the job create/edit form and detail view. Added a Job Match page that compares comma/newline-separated user and job skill lists case-insensitively, removes duplicates, calculates matched-required percentages, and ranks active jobs.
- Added the `required_skills` column to the fresh-install schema and provided a one-time migration for existing databases.

**Changes and Modifications:**
- AI modified `app.py`, `schema.sql`, `README.md`, `templates/base.html`, `templates/jobs.html`, `templates/job_detail.html`, and `static/style.css`; created `templates/dashboard.html`, `templates/job_match.html`, and `migration_add_required_skills.sql`; updated this log. No student modifications are confirmed.

**Files Affected:**
- `app.py`, `schema.sql`, `README.md`, `templates/base.html`, `templates/jobs.html`, `templates/job_detail.html`, and `static/style.css` (modified).
- `templates/dashboard.html`, `templates/job_match.html`, and `migration_add_required_skills.sql` (created).
- `AI_USAGE.md` (updated).

**Testing and Verification:**
- Ran `git diff --check`; no whitespace errors were reported.
- Did not run the Flask app, apply the database migration, or exercise the dashboard or matching page against MySQL.

**What Worked Well:**
- The match percentage has a clear denominator: the job's listed required skills. Jobs without skill data remain visible but are shown as unscored.

**Lessons Learned:**
- Existing databases need the included one-time migration before using the new required-skills field; pending student reflection on the feature implementation.

### 2026-11-17 — Document project setup in README

**AI Tool:** Codex (GPT-6 Thinking)

**Purpose:** Document how to install dependencies, configure environment variables, initialize the MySQL database, and run the Flask app.

**Key Prompt(s):**
- "update the README with setup instructions"

**AI Contribution:**
- Added setup instructions for cloning the project, creating a virtual environment on macOS/Linux or Windows, installing dependencies, configuring `.env`, creating or migrating the database, optionally loading sample data, and starting Flask.
- Documented Job Match input format and percentage calculation, plus the need to run the skills migration once on an existing database.

**Changes and Modifications:**
- AI rewrote `README.md` and updated this log. No student modifications are confirmed.

**Files Affected:**
- `README.md` (rewritten).
- `AI_USAGE.md` (updated).
- `.env.example`, `requirements.txt`, `schema.sql`, `migration_add_required_skills.sql`, `seed.sql`, `database.py`, and `app.py` (reviewed to align instructions; unchanged in this task).

**Testing and Verification:**
- Ran `git diff --check`; no whitespace errors were reported.
- Did not run setup commands or connect to MySQL.

**What Worked Well:**
- The guide distinguishes new database setup from upgrading an existing database and calls out that the seed script should only be used once on an empty database.

**Lessons Learned:**
- Pending student reflection.

### 2026-11-17 — Show flash messages as toast notifications

**AI Tool:** Codex (GPT-6 Thinking)

**Purpose:** Keep success messages from shifting page content and have them dismiss automatically after about five seconds.

**Key Prompt(s):**
- "I don't don't like these company added message? it moves the entire screen, could it be added like a toast, that dissapears in 5 seconds or so"

**AI Contribution:**
- Moved Flask flash messages into a fixed-position toast container that overlays the page.
- Added a close button for each toast and automatic dismissal after five seconds for success and informational messages. Error messages remain until manually dismissed.
- Added responsive positioning and reduced-motion support.

**Changes and Modifications:**
- AI modified `templates/base.html`, `static/style.css`, and this log; created `static/app.js`. No student modifications are confirmed.

**Files Affected:**
- `templates/base.html` and `static/style.css` (modified).
- `static/app.js` (created).
- `AI_USAGE.md` (updated).

**Testing and Verification:**
- Ran `git diff --check`; no whitespace errors were reported.
- Did not run the app or verify the toast in a browser.

**What Worked Well:**
- Flash messages are positioned outside the normal page layout, so they no longer move the page content.

**Lessons Learned:**
- Pending student reflection.
