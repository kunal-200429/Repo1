# Expense Tracker with WhatsApp Notifications & Web Interface

A comprehensive Python application to track daily expenses with categories, CLI interface, REST API, web dashboard, and WhatsApp notifications. All amounts displayed in Indian Rupees (₹).

## Features

- **Web Dashboard** - Visual interface accessible via browser at http://127.0.0.1:5000/
- Add, list, filter, delete, and export expenses
- Categories management (add/list categories)
- Daily/weekly/monthly summaries with category breakdowns
- CSV export for spreadsheet analysis
- CLI commands using Typer
- REST API using Flask
- WhatsApp notifications via pywhatkit
- Responsive web design (works on mobile/desktop)
- SQLite database with automatic table creation

## Installation

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Web Interface (Recommended)

Start the web server with full interface:
```
python main.py web
```

Open your browser to `http://127.0.0.1:5000/` for:
- Dashboard with expense overview and recent transactions
- Add expenses with optional WhatsApp notifications
- View and filter all expenses
- Generate summaries and reports
- Export data to CSV

### CLI

Run CLI commands:
```
python main.py cli
```

Available commands:
- `add <amount> <category> [description] [--notify phone]` - Add new expense
- `list [--category CATEGORY] [--date DATE]` - List/filter expenses
- `summary [daily|weekly|monthly]` - View expense summaries
- `export [filename]` - Export expenses to CSV
- `add-category <name>` - Add new category
- `list-categories` - List all categories
- `delete <id>` - Delete expense by ID

Examples:
```bash
# Add expense with WhatsApp notification
python cli.py add 25.99 entertainment "Movie tickets" --notify +1234567890

# List food expenses
python cli.py list --category food

# Get weekly summary
python cli.py summary weekly

# Export to custom file
python cli.py export my_expenses.csv
```

### REST API

The API is available when running the web server at `http://127.0.0.1:5000/api/`

API endpoints:
- `GET /api/expenses` - List expenses (query params: category, date)
- `POST /api/expenses` - Add expense (JSON body: amount, category, description, date)
- `DELETE /api/expenses/<id>` - Delete expense by ID

API examples:
```bash
# List all expenses
curl http://127.0.0.1:5000/api/expenses

# Add expense
curl -X POST http://127.0.0.1:5000/api/expenses \
  -H "Content-Type: application/json" \
  -d '{"amount": 15.50, "category": "food", "description": "Coffee"}'

# Filter by category
curl "http://127.0.0.1:5000/api/expenses?category=food"
```

## WhatsApp Notifications

To enable WhatsApp notifications:

1. **Install WhatsApp Desktop** on your computer (download from whatsapp.com/download)
2. **Log into WhatsApp Web** in your browser:
   - Go to https://web.whatsapp.com
   - Scan the QR code with WhatsApp on your phone
3. **Keep WhatsApp Web open** in your browser during use
4. When adding expenses, provide phone number in international format (e.g., +1234567890)

**Important Notes:**
- pywhatkit requires WhatsApp Web to be running and logged in
- First message may take longer as it opens WhatsApp Web
- Phone number must include country code (e.g., +1 for US, +91 for India)
- If notifications fail, check that WhatsApp Web is logged in and accessible

**Troubleshooting:**
- Make sure WhatsApp Web is open in your browser
- Ensure your phone number is in the correct international format
- Check browser console for any JavaScript errors
- Try refreshing WhatsApp Web if messages aren't sending

## Database

Uses SQLite (`expenses.db`) created automatically. Tables:
- `expenses`: id, amount, category, description, date
- `categories`: id, name

## Project Structure

```
expense_tracker/
├── main.py              # Entry point (CLI/Web selection)
├── cli.py               # CLI interface using Typer
├── api.py               # Flask web app with API and web routes
├── database.py          # SQLite database operations
├── models.py            # Data models (Expense, Category)
├── utils.py             # Helper functions (export, summaries)
├── whatsapp.py          # WhatsApp notification functions
├── requirements.txt     # Python dependencies
├── templates/           # HTML templates for web interface
│   ├── base.html        # Base template with navigation
│   ├── index.html       # Dashboard page
│   ├── add_expense.html # Add expense form
│   ├── expenses.html    # List/filter expenses
│   ├── summary.html     # Summary reports
│   └── export.html      # Export functionality
├── expenses.db          # SQLite database (auto-created)
├── expenses.csv         # Export file
└── PyWhatKit_DB.txt     # WhatsApp session data
```

## Future Enhancements

- User authentication and multi-user support
- Budget setting and spending alerts
- Recurring expenses
- Receipt photo uploads
- Advanced analytics and charts
- Mobile app companion
- Cloud backup and sync
- Email notifications alternative
- Multi-currency support
