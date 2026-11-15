# AGENTS.md — Project AI Instructions

## Project Context

This repository contains the COP4751 Database Systems course project: **Job Application Tracker**.

The application uses:
- MySQL for the database
- Python and Flask for the backend
- HTML and CSS for the frontend
- GitHub for version control

AI tools are permitted and encouraged for development, debugging, explanations, and code review. However, all AI assistance must be documented in `AI_USAGE.md`, as required by the course project specification.

## Mandatory Rule: Maintain AI_USAGE.md

**Every AI assistant working on this repository MUST maintain the `AI_USAGE.md` file.**

This requirement applies to ChatGPT, Claude, Codex, Gemini, Copilot, and any other AI coding assistant that reads these instructions.

### When to Update

Update `AI_USAGE.md` during every AI-assisted development task, including:

- Writing, generating, or modifying code
- Debugging errors
- Reviewing existing code
- Creating database schemas or SQL queries
- Implementing Flask routes
- Building HTML/CSS interfaces
- Designing algorithms, including the Job Match feature
- Refactoring or optimizing code
- Creating or modifying tests
- Explaining concepts that influence implementation
- Making architectural or design decisions

An update is required even if the AI only provided suggestions and did not modify any files.

Group related back-and-forth messages into one meaningful task entry rather than creating an entry for every individual message.

### Required Workflow

For every task:

1. Read `AI_USAGE.md` before beginning work, if it exists.
2. Complete the requested task.
3. Identify the AI assistance that was provided.
4. Create `AI_USAGE.md` if it does not exist.
5. Update the file with a factual record of the completed task.
6. Preserve all previous documentation.
7. Finish the documentation update before reporting the task as completed.

**Do not consider an AI-assisted task complete until its AI usage has been documented.**

When possible, include the documentation update in the same commit as the related code changes.

## Required AI_USAGE.md Structure

The file must contain the following sections:

### 1. Tools Used

Maintain a cumulative list of AI tools used in the project.

For each tool, document:
- Tool name
- Model name, if known
- How the tool was used

Add new tools as they are introduced. Do not duplicate existing entries.

### 2. Key Prompts

Document important prompts used to obtain AI assistance.

- Preserve the exact wording of important prompts when available.
- Otherwise, provide an accurate summary.
- Include sufficient context to explain what was requested.
- Never invent prompts or claim an exact quotation when the original wording is unavailable.

### 3. What Worked Well

Document useful AI contributions, such as:
- Code that worked correctly
- Successful debugging assistance
- Helpful explanations
- Useful implementation suggestions
- Improvements to application design

Describe what actually worked rather than assuming AI output was successful.

### 4. What I Modified

Document modifications made to AI-generated code or suggestions.

Examples:
- Adjusting SQL queries to match the database schema
- Fixing errors in AI-generated code
- Adding missing validation
- Changing application logic
- Improving generated HTML/CSS
- Rejecting or replacing an AI suggestion

Clearly distinguish changes performed by the AI assistant from changes made independently by the student.

If no student modifications are known, state that they have not been documented or confirmed. Never invent manual modifications.

### 5. Lessons Learned

Document confirmed lessons from using AI, such as:
- Why testing AI-generated code is important
- How better prompts improve results
- Limitations or mistakes encountered
- Concepts clarified through AI assistance
- How AI contributed to understanding the implementation

Do not invent personal learning experiences. If the student's reflection is unknown, mark it for student review.

### 6. Detailed AI Usage Log

Maintain a chronological log of AI-assisted tasks using the following format.

---

## AI Usage Entry Template

### YYYY-MM-DD — Task Title

**AI Tool:** Tool name and model, if known

**Purpose:** Brief description of the task.

**Key Prompt(s):**
- Exact prompt or accurate summary of the request.

**AI Contribution:**
- What code, suggestions, explanations, or ideas the AI provided.
- What parts of the implementation were AI-assisted.

**Changes and Modifications:**
- Changes made to the generated output.
- Corrections or improvements applied.
- Student changes, only when confirmed.

**Files Affected:**
- List of files created, modified, or reviewed.
- Write "None" if no files were changed or reviewed.

**Testing and Verification:**
- Tests or commands actually executed.
- Results of those tests.
- Known issues or limitations.
- If no tests were executed, explicitly state that.

**What Worked Well:**
- Successful AI contributions supported by actual results.

**Lessons Learned:**
- Confirmed insights, or "Pending student reflection."

---

## Documentation Rules

1. **Never delete previous entries.** Preserve the complete history of AI assistance.

2. **Never fabricate information.** Only document work, prompts, modifications, and testing that actually occurred or are supported by the available context.

3. **Use the real date.** Record the date when AI assistance occurred, using `YYYY-MM-DD`.

4. **Be specific.** Prefer "Generated a Flask route for editing company records" over "Helped with Python."

5. **Track AI-generated code accurately.** Identify which files or functions were created or modified with AI assistance.

6. **Record failures as well as successes.** If generated code failed or required corrections, document those issues.

7. **Preserve existing content.** Append new chronological entries and update cumulative summary sections without overwriting prior entries.

8. **Avoid unnecessary duplication.** Related prompts and changes from one task can be grouped into a single entry.

9. **Protect sensitive information.** Do not include passwords, API keys, database credentials, or other secrets in the documentation.

10. **Keep documentation readable.** Use proper Markdown headings, concise explanations, and consistent formatting.

11. **Do not claim tests passed unless they were executed.** Clearly distinguish tested results from suggestions or assumptions.

12. **Do not rewrite the documentation history to make AI contributions appear smaller or larger than they were.**

## Automatic File Initialization

If `AI_USAGE.md` does not exist, create it with these headings:

# AI Usage Documentation

## Tools Used

## Key Prompts

## What Worked Well

## What I Modified

## Lessons Learned

## Detailed AI Usage Log

After initialization, add the first documented AI usage entry.

## Final Task Checklist

Before completing any task, verify:

- [ ] `AI_USAGE.md` exists.
- [ ] The current AI-assisted task is documented.
- [ ] The tool and important prompts are recorded.
- [ ] AI-generated code, ideas, or recommendations are described.
- [ ] Changes to AI output are documented accurately.
- [ ] Actual testing results are recorded.
- [ ] Lessons learned are documented or marked for student review.
- [ ] Previous documentation remains intact.

## Priority

Maintaining `AI_USAGE.md` is a mandatory project requirement, not an optional task.

Whenever an AI assistant contributes to this repository, it must maintain this documentation as part of its normal workflow.

If the assistant cannot write to the repository, it must provide the corresponding Markdown entry for the student to add manually, and explicitly state that it could not update the file.

**The goal is to produce an accurate, complete, continuously maintained record of AI assistance that satisfies the COP4751 course project's GenAI documentation requirements.**