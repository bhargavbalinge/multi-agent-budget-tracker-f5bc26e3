
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory data store (for demonstration purposes)
data = {
    "total_budget": 1000,
    "expenses": [
        {"description": "Groceries", "amount": 150},
        {"description": "Rent", "amount": 500},
    ]
}

@app.route('/')
def index():
    return render_template('index.html', data=data)

@app.route('/api/v1/expenses', methods=['POST'])
def add_expense():
    new_expense = request.get_json()
    data['expenses'].append(new_expense)
    return jsonify({"message": "Expense added successfully!"})

# This is the corrected budget calculation function
def calculate_remaining_budget(total_budget, expenses):
  """
  This function calculates the remaining budget by subtracting the total expenses from the total budget.
  """
  total_expenses = sum(expense['amount'] for expense in expenses)
  remaining_budget = total_budget - total_expenses
  return remaining_budget

@app.route('/api/v1/budget-data')
def get_budget_data():
    remaining_budget = calculate_remaining_budget(data['total_budget'], data['expenses'])
    return jsonify({
        "total_budget": data["total_budget"],
        "expenses": data["expenses"],
        "remaining_budget": remaining_budget
    })

if __name__ == '__main__':
    app.run(debug=True)
