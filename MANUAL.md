# Expense Tracker Manual

## Overview

The Expense Tracker is a comprehensive Python application for tracking daily expenses with categories, budgets, and WhatsApp notifications. It features a web interface, CLI commands, REST API, and data persistence using SQLite.

**Key Features:**
- Web dashboard for easy expense management
- CLI interface for quick operations
- REST API for integrations
- WhatsApp notifications for expense alerts
- Category-based expense tracking
- Daily/weekly/monthly summaries
- CSV export functionality
- SQLite database (automatic setup)

## System Requirements

- Python 3.10+
- Windows/Linux/Mac
- Internet connection (for WhatsApp notifications)

## Installation

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

Required packages:
- typer (CLI interface)
- flask (web framework)
- pywhatkit (WhatsApp notifications)

### 2. Verify Installation

```bash
python -c "import flask, typer, pywhatkit; print('All dependencies installed')"
```

## Getting Started

### Quick Start

1. **Navigate to project directory:**
   ```bash
   cd expense_tracker
   ```

2. **Start the web interface:**
   ```bash
   python main.py web
   ```

3. **Open browser:**
   - Go to http://127.0.0.1:5000/
   - Start adding expenses!

## Usage Guide

### Web Interface (Recommended)

#### Starting the Web Server
```bash
python main.py web
```

The web interface provides:
- **Dashboard**: Overview of expenses and recent transactions
- **Add Expense**: Form to add new expenses with WhatsApp notifications
- **View Expenses**: List and filter all expenses
- **Summary**: Daily/weekly/monthly reports
- **Export**: Download expenses as CSV

#### Adding Your First Expense

1. Click "Add New Expense" from dashboard
2. Fill in:
   - Amount (in ₹)
   - Category (select from dropdown or type new)
   - Description (optional)
   - Date (defaults to today)
   - WhatsApp notification (optional)
3. Click "Add Expense"

#### WhatsApp Notifications Setup

1. **Install WhatsApp Desktop** (optional but recommended)
2. **Open WhatsApp Web:**
   - Go to https://web.whatsapp.com
   - Scan QR code with your phone
3. **Keep browser tab open**
4. **Add expense with notification:**
   - Check "Send WhatsApp notification"
   - Enter phone number: +91XXXXXXXXXX (include country code)

### CLI Interface

#### Starting CLI Mode
```bash
python main.py cli
```

#### Available Commands

```bash
# Add expense
python cli.py add 250.00 food "Lunch at restaurant" --notify +919876543210

# List expenses
python cli.py list
python cli.py list --category food
python cli.py list --date 2024-01-15

# View summaries
python cli.py summary daily
python cli.py summary weekly
python cli.py summary monthly

# Export to CSV
python cli.py export
python cli.py export my_expenses.csv

# Manage categories
python cli.py add-category transportation
python cli.py list-categories

# Delete expense
python cli.py delete 1
```

### REST API

The API is available when web server is running at `http://127.0.0.1:5000/api/`

#### Endpoints

- **GET /api/expenses** - List expenses
  - Query params: `category`, `date`
  - Example: `GET /api/expenses?category=food`

- **POST /api/expenses** - Add expense
  - Body: `{"amount": 100.50, "category": "food", "description": "Coffee"}`

- **DELETE /api/expenses/<id>** - Delete expense

#### API Examples

```bash
# List all expenses
curl http://127.0.0.1:5000/api/expenses

# Add expense
curl -X POST http://127.0.0.1:5000/api/expenses \
  -H "Content-Type: application/json" \
  -d '{"amount": 150.00, "category": "shopping", "description": "New shirt"}'

# Filter by category
curl "http://127.0.0.1:5000/api/expenses?category=food"
```

## Database

### SQLite Database

- **File**: `expenses.db` (created automatically)
- **Tables**:
  - `expenses`: id, amount, category, description, date
  - `categories`: id, name

### Backup

To backup your data:
```bash
cp expenses.db expenses_backup.db
```

## WhatsApp Notifications

### Setup Process

1. **Prerequisites:**
   - WhatsApp account
   - Phone with WhatsApp installed
   - Web browser

2. **Steps:**
   - Open https://web.whatsapp.com
   - Scan QR code with phone
   - Keep browser tab open
   - Test with any expense addition

3. **Phone Number Format:**
   - Must include country code
   - Examples: +91 for India, +1 for US
   - Format: +[country code][phone number]

### Troubleshooting WhatsApp

**Issue: "WhatsApp notification failed"**
- Ensure WhatsApp Web is open and logged in
- Check phone number format (+91XXXXXXXXXX)
- Try refreshing WhatsApp Web
- Check browser console for errors

**Issue: Messages not sending**
- Verify WhatsApp Web is active
- Ensure phone has internet connection
- Try closing and reopening WhatsApp Web

## File Structure

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
├── MANUAL.md           # This manual
├── README.md           # Project README
├── templates/          # HTML templates for web interface
│   ├── base.html       # Base template with navigation
│   ├── index.html      # Dashboard page
│   ├── add_expense.html# Add expense form
│   ├── expenses.html   # List/filter expenses
│   ├── summary.html    # Summary reports
│   └── export.html     # Export functionality
├── expenses.db         # SQLite database (auto-created)
├── expenses.csv        # Export file (generated)
└── PyWhatKit_DB.txt    # WhatsApp session data
```

## Common Issues & Solutions

### Web Server Won't Start
```bash
# Check if port 5000 is in use
netstat -ano | findstr :5000

# Kill process if needed
taskkill /PID <PID> /F

# Or use different port
python -c "from api import app; app.run(port=5001)"
```

### Database Issues
```bash
# Reset database
rm expenses.db
python -c "from database import create_tables; create_tables()"
```

### Import Errors
```bash
# Reinstall dependencies
pip uninstall -r requirements.txt -y
pip install -r requirements.txt
```

### WhatsApp Not Working
- Ensure WhatsApp Web is open
- Check phone number format
- Try refreshing browser
- Verify internet connection

## Tips & Best Practices

### Expense Tracking
- Use consistent categories
- Add descriptions for better tracking
- Set up WhatsApp notifications for large expenses
- Review weekly summaries

### Data Management
- Export data regularly as CSV
- Backup `expenses.db` file
- Use meaningful category names

### Performance
- Keep database file in project directory
- Close web server when not in use
- Clear browser cache if web interface is slow

## Support

If you encounter issues:
1. Check this manual first
2. Review error messages in terminal/console
3. Ensure all dependencies are installed
4. Try restarting the application
5. Check WhatsApp Web is properly logged in

## Version History

- **v1.0**: Initial release with web interface, CLI, API, and WhatsApp notifications
- Features: Expense tracking, categories, summaries, CSV export, SQLite database

---

**Happy expense tracking!** 📊💰📱
