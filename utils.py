import csv
from collections import defaultdict
from datetime import datetime, timedelta
from database import get_expenses

def export_to_csv(filename='expenses.csv'):
    expenses = get_expenses()
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['id', 'amount', 'category', 'description', 'date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for exp in expenses:
            writer.writerow(exp.to_dict())

def get_summary(period='daily'):
    expenses = get_expenses()
    summary = defaultdict(float)
    total = 0.0
    now = datetime.now()
    if period == 'daily':
        start_date = now.strftime('%Y-%m-%d')
        filtered = [e for e in expenses if e.date == start_date]
    elif period == 'weekly':
        start_date = (now - timedelta(days=7)).strftime('%Y-%m-%d')
        filtered = [e for e in expenses if e.date >= start_date]
    elif period == 'monthly':
        start_date = (now - timedelta(days=30)).strftime('%Y-%m-%d')
        filtered = [e for e in expenses if e.date >= start_date]
    else:
        filtered = expenses

    for exp in filtered:
        summary[exp.category] += exp.amount
        total += exp.amount

    return {'total': total, 'by_category': dict(summary), 'expenses': [e.to_dict() for e in filtered]}
