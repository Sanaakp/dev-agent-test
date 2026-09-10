# General Project Rules

## Purpose

Keep the project clear, predictable, and easy to change. Prefer small, focused changes over broad rewrites.

## Structure

- Keep the main application entry point in `main.py`.
- Keep JavaScript behavior in focused modules such as `app.js`.
- Group tests separately from application code.
- Do not add generated files, local caches, or secrets to source control.

## Python

- Target the Python version documented by the project.
- Use type hints for public functions and meaningful return values.
- Keep functions small and give them one responsibility.
- Keep reusable result-building logic in focused Python modules instead of the CLI entry point.
- Use the standard library unless a dependency provides clear value.
- Return non-zero exit codes for command-line failures.

## JavaScript

- Use strict mode and modern, readable JavaScript.
- Prefer `const`; use `let` only when reassignment is required.
- Keep side effects at the application boundary.
- Export reusable behavior so it can be tested.
- Avoid adding a framework without a concrete project need.

## Quality

- Add or update focused tests for behavior changes.
- Run syntax checks and the relevant test suite before submitting changes.
- Keep formatting consistent with nearby code.
- Do not silence errors without documenting the reason.

## Security

- Never commit passwords, tokens, private keys, or personal data.
- Validate input at application boundaries.
- Do not execute untrusted input as code or shell commands.
- Log useful diagnostic context without exposing secrets.

## Change Process

1. Identify the smallest owning module.
2. Make the smallest change that solves the problem.
3. Verify the changed behavior.
4. Update documentation when the public behavior changes.
