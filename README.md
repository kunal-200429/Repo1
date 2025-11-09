 Expense Tracker with WhatsApp

Track daily expenses, categories, and budgets with a simple Python service that can send WhatsApp notifications and summaries to your phone. This project supports CLI and REST usage, persists data to SQLite/PostgreSQL, and integrates WhatsApp via Twilio or a headless web automation option.
 Features
- Add, list, filter, and export expenses with categories, notes, and dates.
- Daily/weekly/monthly summaries with totals and category breakdowns.
- WhatsApp notifications for new expenses and scheduled summaries.
- CSV import/export and simple SQLite by default; PostgreSQL optional.
- CLI commands and REST API with token auth.

Tech stack
- Python 3.10+ (Typer/Click for CLI, FastAPI for API, SQLAlchemy for ORM).
- SQLite (dev) / PostgreSQL (prod).
- Twilio WhatsApp API for messaging; alternative pywhatkit for local automation.

 Table of contents
- Getting started
- Quick start
- Configuration
- CLI usage
- REST API
- WhatsApp setup
- Scheduling
- Data model
- CSV import/export
- Testing
- Docker
- Deployment
- Roadmap
- Contributing
- License

 Getting started
This project follows common Python README best practices: clear setup, commands, and environment configuration. Ensure Python 3.10+ is installed.

Prerequisites
- Python 3.10+ and pip.
- Twilio account (for WhatsApp API) or local browser automation alternative.
- Git.

Clone and setup
- git clone <your-repo-url>
- cd expense-tracker-whatsapp
- python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
- pip install -r requirements.txt

Quick start
- Copy .env.example to .env and fill values (see Configuration).
- Initialize database:
  - python -m app.db init
  - python -m app.db migrate
  - python -m app.db upgrade
- Run CLI help:
  - python -m app.cli --help
- Start API:
  - uvicorn app.api:app --reload

Send a WhatsApp test message (Twilio sandbox):
- python -m app.whatsapp send --to "whatsapp:+<E164_NUMBER>" --text "Hello from Expense Tracker!"

 Configuration
Create a .env file with the following keys. Example values align with Twilio’s WhatsApp sandbox and standard DB settings.
Required
- DATABASE_URL=sqlite:///./expense.db
- SECRET_TOKEN=change-me
- TZ=Asia/Kolkata

WhatsApp via Twilio
- TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
- TWILIO_AUTH_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
- TWILIO_WHATSAPP_FROM=whatsapp:+14155238886
- WHATSAPP_TO=whatsapp:+91XXXXXXXXXX

Optional (automation alternative)
- USE_PYWHATKIT=true
- PYWHATKIT_HEADLESS=false

 CLI usage
The CLI provides expense commands, summaries, and WhatsApp actions. It’s implemented with Typer/Click patterns consistent with Python CLI norms.
Examples
- Add an expense:
  - python -m app.cli add --amount 299.00 --category "Food" --note "Dinner" --date 2025-10-18
- List expenses:
  - python -m app.cli list --from 2025-10-01 --to 2025-10-31 --category Food
- Monthly summary:
  - python -m app.cli summary --period month
- Export to CSV:
  - python -m app.cli export --out expenses_oct.css
- Send WhatsApp summary:
  - python -m app.whatsapp summary --period week

REST API
The API uses FastAPI. Provide X-API-KEY: <SECRET_TOKEN> in headers.

Endpoints
- GET /health → {status:"ok"}
- GET /expenses?from=&to=&category=
- POST /expenses {amount, category, note, date}
- GET /summary?period=day|week|month
- POST /notify/expense {id}
- POST /notify/summary {period}

Run locally
- uvicorn app.api:app --reload
- Visit /docs for OpenAPI UI.

 WhatsApp setup
Using Twilio (recommended)
1. Create a Twilio account and enable the WhatsApp Sandbox.
2. Join the sandbox by sending the provided keyword to the sandbox number.
3. Set environment variables for Account SID, Auth Token, from number, and to number with whatsapp: prefix in E.164 format.
4. Test message using python -m app.whatsapp send.

Notes
- Use parameter from_ in Python clients to avoid Python keyword conflict.
- Content templates and media messages are supported; see Twilio docs for media.

Alternative: pywhatkit (local automation)
- pip install pywhatkit
- Requires active WhatsApp Web session in browser; useful for personal projects and demos.

 Scheduling
Schedule daily/weekly summaries via cron or Windows Task Scheduler.
- Example cron (7:30 PM daily):
  - 30 19 * * * cd /path/to/app && . .venv/bin/activate && python -m app.whatsapp summary --period day

Data model
Core tables
- expenses: id, amount, category, note, date, created_at.
- categories: id, name, budget_monthly (optional).

Summary logic
- Period aggregation over date range: sum(amount), count, top categories.

 CSV import/export
- Import: python -m app.cli import --file expenses.csv
  - Expects header: Date,Category,Description,Amount.
- Export: python -m app.cli export --out out.csv

 Testing
- Install dev deps: pip install -r requirements-dev.txt
- Run tests: pytest -q
- Lint: ruff check . && black --check .

 Docker
Build
- docker build -t expense-tracker-whatsapp .
Run
- docker run --env-file .env -p 8000:8000 expense-tracker-whatsapp uvicorn app.api:app --host 0.0.0.0 --port 8000

 Deployment
- Set DATABASE_URL to managed Postgres in production.
- Store secrets as environment variables, not in code.
- For Twilio production WhatsApp, register a WhatsApp Business account and templates.

 Roadmap
- Budgets and alerts when exceeding category/month limits.
- Media receipts via WhatsApp, OCR extraction.
- Multi-user with OAuth and per-user WhatsApp routing.
- Web dashboard with charts.

 References
- Python README best practices and structure.
- General README template ideas.
- Twilio WhatsApp quickstart and media messaging.
- WhatsApp message sending tips in Python (from_ param).
- pywhatkit automation for WhatsApp.
- CSV-based expense tracker walkthrough for ideas.

