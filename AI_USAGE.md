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
- Asked for a commit message for the current backend and environment configuration changes.

## What Worked Well

- Repository inspection identified two untracked documentation files and no tracked changes, supporting a documentation-focused commit message.

## What I Modified

- The AI assistant populated the previously empty `AI_USAGE.md`. Independent student modifications have not been documented or confirmed.
- The AI assistant created `schema.sql` from the user-provided schema; no independent student edits to that output are confirmed.

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
