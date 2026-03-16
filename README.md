
# Budget Tracker Web App

This is a simple web application for tracking your budget, expenses, and income.

## Setup

1.  **Clone the repository:**

    ```
    git clone https://github.com/your-username/budget-tracker.git
    ```

2.  **Install the dependencies:**

    ```
    pip install -r requirements.txt
    ```

3.  **Initialize the database:**

    ```
    python -c "from app import db, app; app.app_context().push(); db.create_all()"
    ```

4.  **Run the application:**

    ```
    python app.py
    ```

## Usage

1.  Create an account or log in.
2.  Define your monthly budget and allocate amounts to different categories.
3.  Record your expenses and income.
4.  View reports on your spending habits.
