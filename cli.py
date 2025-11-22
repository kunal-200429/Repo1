import typer
from models import Expense, Category
from database import add_expense, get_expenses, add_category, get_categories, create_tables, delete_expense
from utils import export_to_csv, get_summary
from whatsapp import send_whatsapp_message

app = typer.Typer()

@app.callback()
def callback():
    create_tables()

@app.command()
def add(amount: float, category: str, description: str = "", date: str = typer.Option(None, "--date"), notify: str = typer.Option(None, "--notify")):
    """
    Add a new expense. Optionally notify via WhatsApp (provide phone number).
    """
    expense = Expense(amount=amount, category=category, description=description, date=date)
    add_expense(expense)
    typer.echo(f"Expense added: {expense.amount} for {expense.category}")
    if notify:
        message = f"New expense: {expense.amount} for {expense.category} - {expense.description}"
        send_whatsapp_message(notify, message)

@app.command()
def list(category: str = typer.Option(None, "--category"), date: str = typer.Option(None, "--date")):
    """
    List expenses, optionally filter by category or date.
    """
    expenses = get_expenses(category=category, date=date)
    if not expenses:
        typer.echo("No expenses found.")
        return
    for exp in expenses:
        typer.echo(f"{exp.id}: {exp.amount} - {exp.category} - {exp.description} - {exp.date}")

@app.command()
def export(filename: str = typer.Option('expenses.csv', "--filename")):
    """
    Export expenses to CSV.
    """
    export_to_csv(filename)
    typer.echo(f"Expenses exported to {filename}")

@app.command()
def summary(period: str = typer.Option('daily', help='daily, weekly, or monthly')):
    """
    Show expense summary for the period.
    """
    summ = get_summary(period)
    typer.echo(f"Total: {summ['total']}")
    typer.echo("By category:")
    for cat, amt in summ['by_category'].items():
        typer.echo(f"  {cat}: {amt}")

@app.command()
def add_new_category(name: str):
    """
    Add a new category.
    """
    category = Category(name=name)
    add_category(category)
    typer.echo(f"Category added: {category.name}")

@app.command()
def list_categories():
    """
    List all categories.
    """
    categories = get_categories()
    for cat in categories:
        typer.echo(f"{cat.id}: {cat.name}")

@app.command()
def delete(expense_id: int):
    """
    Delete an expense by ID.
    """
    if delete_expense(expense_id):
        typer.echo(f"Expense {expense_id} deleted.")
    else:
        typer.echo(f"Expense {expense_id} not found.")

if __name__ == "__main__":
    app()
