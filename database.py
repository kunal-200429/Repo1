import sqlite3
from models import Expense, Category

DB_NAME = 'expenses.db'

def create_tables():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_expense(expense):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)',
                   (expense.amount, expense.category, expense.description, expense.date))
    conn.commit()
    expense.id = cursor.lastrowid
    conn.close()
    return expense

def get_expenses(category=None, date=None):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    query = 'SELECT id, amount, category, description, date FROM expenses'
    params = []
    if category:
        query += ' WHERE category = ?'
        params.append(category)
    if date:
        if category:
            query += ' AND date = ?'
        else:
            query += ' WHERE date = ?'
        params.append(date)
    query += ' ORDER BY date DESC'
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    return [Expense(id=r[0], amount=r[1], category=r[2], description=r[3], date=r[4]) for r in rows]

def add_category(category):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO categories (name) VALUES (?)', (category.name,))
        conn.commit()
        category.id = cursor.lastrowid
    except sqlite3.IntegrityError:
        pass  # Category already exists
    conn.close()
    return category

def get_categories():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT id, name FROM categories')
    rows = cursor.fetchall()
    conn.close()
    return [Category(id=r[0], name=r[1]) for r in rows]

def delete_expense(expense_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
    deleted = cursor.rowcount > 0
    conn.commit()
    conn.close()
    return deleted
