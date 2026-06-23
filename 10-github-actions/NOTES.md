## L10 — github-actions

**What I built:** Added a CI pipeline to the repo using GitHub Actions. On every pull request to main, it automatically runs ruff (linter) and pytest against the Task 2 (csv-stats) code, so broken or unlinted code is caught before merging.

**What I learned:**
- GitHub Actions basics: workflows live in .github/workflows/*.yml, written in YAML (2-space indentation, not 4 like Python)
- on: pull_request: branches: [main] — triggering a workflow on every PR targeting main (and that it re-runs automatically on each new push to an open PR, no need to recreate the PR)
- jobs / steps structure, runs-on: ubuntu-latest (runs on GitHub's servers, not my machine)
- uses (prebuilt actions like actions/checkout, actions/setup-python) vs run (arbitrary shell commands)
- ruff — a fast Python linter that checks code style without executing it
- working-directory — running a step inside a specific subfolder, so relative paths (like data.csv) resolve correctly
- the difference between local runs and CI runs: CI starts in the repo root, so code relying on relative paths can behave differently than it does locally

**Where I got stuck:**
- typo: pip instal (missing l) made the install step fail
- the first green-ish run still failed at the test step: FileNotFoundError: 'data.csv' — because pytest ran from the repo root, not from inside 02-csv-stats where data.csv lives
- after adding working-directory: 02-csv-stats, the command still had the redundant path (pytest 02-csv-stats -v), so it looked for the folder inside itself — fixed by changing it to just pytest -v
- spent time confused about why no new run appeared, before realizing pushing to the same branch updates the existing PR and re-triggers CI (and that the browser page just needed refreshing)

**Time spent:** ~1 hours