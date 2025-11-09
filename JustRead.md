Expense Tracker with WhatsApp - Project Presentation
Project Overview
This is a beginner-friendly Python application called Expense Tracker with WhatsApp Integration. It allows users to track daily expenses, categorize them, generate summaries, and send notifications via WhatsApp. The project uses simple, built-in Python modules where possible, making it easy for beginners to understand and modify.

Key Features
Add Expenses: Record expenses with amount, category, description, and date.
List and Filter: View all expenses or filter by category/date.
Summaries: Get daily, weekly, or monthly totals and breakdowns by category.
Export: Export expenses to CSV for analysis.
Categories: Manage expense categories.
WhatsApp Notifications: Send instant messages for new expenses (requires WhatsApp Web setup).
CLI Interface: Command-line tools for easy use.
REST API: Simple web API for integration with other apps.
Tech Stack (Beginner-Friendly)
Python 3.10+: Core language.
SQLite3: Built-in database for data persistence.
Typer: For CLI commands (simple and intuitive).
Flask: Lightweight web framework for API.
PyWhatKit: For WhatsApp automation (opens WhatsApp Web).
Project Structure
The project is organized in a single expense_tracker/ directory with these files:

requirements.txt: Lists dependencies (typer, flask, pywhatkit).
models.py: Defines Expense and Category classes with basic attributes.
database.py: Handles SQLite database operations (create tables, add/get expenses/categories).
utils.py: Utilities for CSV export and generating summaries.
whatsapp.py: Function to send WhatsApp messages.
cli.py: CLI commands using Typer (add, list, summary, export, etc.).
api.py: Flask app with REST endpoints (GET/POST /expenses).
main.py: Entry point to run CLI or start API server.
README.md: Instructions on how to run and use the project.
TODO.md: Development checklist.
How It Works
Database: Uses SQLite (expenses.db) to store expenses and categories. Tables are created automatically on first run.
CLI Usage: Run commands like python main.py cli add 50.0 food "Lunch at cafe" to add expenses.
API Usage: Start the server with python main.py api, then use tools like Postman to send requests to http://localhost:5000/expenses.
WhatsApp: For notifications, provide a phone number (e.g., +1234567890) when adding an expense. It opens WhatsApp Web and sends a message.
Summaries: Calculate totals and category breakdowns for specified periods.
Running the Project
Install Dependencies: pip install -r requirements.txt
CLI Mode: python main.py cli --help to see commands, e.g., python main.py cli add 100.0 transport "Bus fare"
API Mode: python main.py api to start server, then test with curl: curl http://localhost:5000/expenses
Direct API: python api.py to run Flask directly.
WhatsApp Setup: Ensure WhatsApp Web is logged in on your browser; pywhatkit will open it automatically.
Demo for Presentation
Show adding an expense via CLI and listing them.
Demonstrate API with a POST request.
Export to CSV and show the file.
Generate a summary.
(Optional) Send a WhatsApp message if setup allows.
Challenges and Learnings
Kept it simple: No complex ORMs, just raw SQL.
WhatsApp integration requires manual setup but is easy.
Beginner focus: Clear code, comments, and modular structure.