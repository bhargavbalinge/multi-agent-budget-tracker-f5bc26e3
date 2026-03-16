import json

class Budget:
    def __init__(self, initial_budget, expenses_file='expenses.json'):
        self.initial_budget = initial_budget
        self.expenses_file = expenses_file
        self.expenses = self.load_expenses()

    def load_expenses(self):
        try:
            with open(self.expenses_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_expenses(self):
        with open(self.expenses_file, 'w') as f:
            json.dump(self.expenses, f, indent=4)

    def add_expense(self, category, amount):
        self.expenses.append({'category': category, 'amount': amount})
        self.save_expenses()

    def get_total_expenses(self):
        return sum(expense['amount'] for expense in self.expenses)

    def get_remaining_budget(self):
        return self.initial_budget - self.get_total_expenses()

    def get_expense_by_category(self, category):
        return [expense for expense in self.expenses if expense['category'] == category]

    def get_total_budget(self):
        return self.initial_budget