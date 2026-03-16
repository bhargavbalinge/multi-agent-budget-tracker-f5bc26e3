
document.addEventListener('DOMContentLoaded', function() {
    const expenseForm = document.getElementById('expense-form');

    if (expenseForm) {
        expenseForm.addEventListener('submit', function(e) {
            e.preventDefault();

            const description = document.getElementById('description').value;
            const amount = parseFloat(document.getElementById('amount').value);

            if (description && amount) {
                fetch('/api/v1/expenses', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ description, amount })
                })
                .then(response => response.json())
                .then(data => {
                    console.log(data.message);
                    // Optionally, refresh the page or update the UI dynamically
                    location.reload();
                })
                .catch(error => {
                    console.error('Error adding expense:', error);
                });
            }
        });
    }

    // Fetch and display budget data
    fetch('/api/v1/budget-data')
        .then(response => response.json())
        .then(data => {
            document.getElementById('total-budget').innerText = data.total_budget;
            document.getElementById('remaining-budget').innerText = data.remaining_budget;
            
            const expensesList = document.getElementById('expenses-list');
            data.expenses.forEach(expense => {
                const listItem = document.createElement('li');
                listItem.innerText = `${expense.description}: $${expense.amount}`;
                expensesList.appendChild(listItem);
            });
        });
});
