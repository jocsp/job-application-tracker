# AI Usage Documentation

## Tools Used

- Codex (GPT-6): reviewed repository changes, suggested a commit message, and initialized this usage log.
  Also generated the initial MySQL schema and reviewed it against the requested fields and relationships.

## Key Prompts

- "which should be the commit message for the changes currently done"
- Requested a root-level `schema.sql` defining companies, jobs, applications, and contacts with the supplied columns, types, and foreign keys.
- Asked what `schema.sql` is for and whether it creates the database from scratch.
- Asked whether the project should include a script that inserts dummy data.

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
