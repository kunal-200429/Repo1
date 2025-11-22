from flask import Flask, request, jsonify, render_template, redirect, url_for
from models import Expense
from database import add_expense, get_expenses, create_tables, get_categories, add_category, delete_expense
from utils import get_summary, export_to_csv
from whatsapp import send_whatsapp_message
from datetime import datetime

app = Flask(__name__)

# Initialize database on first request
@app.before_request
def initialize_database():
    create_tables()

@app.route('/')
def index():
    from utils import get_summary
    summary = get_summary('daily')
    categories = get_categories()
    total_expenses = get_expenses()
    recent_expenses = total_expenses[:5]
    return render_template('index.html', summary=summary, categories=categories, total_expenses=total_expenses, recent_expenses=recent_expenses)

@app.route('/add', methods=['GET', 'POST'])
def add_expense_page():
    if request.method == 'POST':
        amount = float(request.form['amount'])
        category = request.form['category']
        description = request.form.get('description', '')
        date = request.form.get('date', datetime.now().strftime('%Y-%m-%d'))
        expense = Expense(amount=amount, category=category, description=description, date=date)
        add_expense(expense)
        add_category(Category(name=category))  # Auto-add category if new
        notify = request.form.get('notify_number')
        if notify:
            message = f"New expense: ₹{expense.amount} for {expense.category} - {expense.description}"
            send_whatsapp_message(notify, message)
        return redirect(url_for('index'))
    categories = get_categories()
    return render_template('add_expense.html', categories=categories)

@app.route('/expenses')
def expenses():
    category = request.args.get('category')
    date = request.args.get('date')
    expenses_list = get_expenses(category=category, date=date)
    categories = get_categories()
    return render_template('expenses.html', expenses=expenses_list, categories=categories)

@app.route('/expenses/<int:expense_id>/delete', methods=['POST'])
def delete_expense_route(expense_id):
    if delete_expense(expense_id):
        return redirect(url_for('expenses'))
    else:
        return "Expense not found", 404

@app.route('/summary')
def summary():
    period = request.args.get('period', 'daily')
    summ = get_summary(period)
    return render_template('summary.html', summary=summ, period=period)

@app.route('/export')
def export():
    export_to_csv()
    return render_template('export.html')

@app.route('/api/expenses', methods=['GET'])
def list_expenses():
    category = request.args.get('category')
    date = request.args.get('date')
    expenses = get_expenses(category=category, date=date)
    return jsonify([exp.to_dict() for exp in expenses])

@app.route('/api/expenses', methods=['POST'])
def add_expense_endpoint():
    data = request.get_json()
    expense = Expense(amount=data['amount'], category=data['category'], description=data.get('description', ''), date=data.get('date'))
    add_expense(expense)
    return jsonify(expense.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)
