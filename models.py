import sqlite3
from datetime import datetime

class Expense:
    def __init__(self, id=None, amount=0.0, category='', description='', date=None):
        self.id = id
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date or datetime.now().strftime('%Y-%m-%d')

    def to_dict(self):
        return {
            'id': self.id,
            'amount': self.amount,
            'category': self.category,
            'description': self.description,
            'date': self.date
        }

class Category:
    def __init__(self, id=None, name=''):
        self.id = id
        self.name = name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
