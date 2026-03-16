import streamlit as st

st.title("Budget Tracker")

# Initialize session state
if 'total_budget' not in st.session_state:
    st.session_state.total_budget = 0.0

if 'categories' not in st.session_state:
    st.session_state.categories = {}

if 'expenses' not in st.session_state:
    st.session_state.expenses = []

# --- Sidebar ---
st.sidebar.header("Settings")
total_budget = st.sidebar.number_input("Enter Total Budget", value=st.session_state.total_budget, step=100.0, min_value=0.0)
if total_budget != st.session_state.total_budget:
    st.session_state.total_budget = total_budget
    st.experimental_rerun()

st.sidebar.header("Add Category")
new_category = st.sidebar.text_input("Category Name")
category_budget = st.sidebar.number_input("Category Budget", value=0.0, step=10.0, min_value=0.0)

if st.sidebar.button("Add Category"):
    if new_category:
        # Bug Fix #9: Prevent category allocation from exceeding total budget
        allocated_budget = sum(st.session_state.categories.values())
        if allocated_budget + category_budget > st.session_state.total_budget:
            st.sidebar.error("Category budget allocation cannot exceed total budget.")
        else:
            st.session_state.categories[new_category] = category_budget
            st.experimental_rerun()

# --- Main Page ---
st.header("Budget Overview")

# Bug Fix #10: Correct remaining budget calculation
total_expenses = sum(expense['amount'] for expense in st.session_state.expenses)
remaining_budget = st.session_state.total_budget - total_expenses

st.write(f"Total Budget: ${st.session_state.total_budget:.2f}")
st.write(f"Total Expenses: ${total_expenses:.2f}")
st.write(f"Remaining Budget: ${remaining_budget:.2f}")


st.header("Category Allocation")
allocated_budget = sum(st.session_state.categories.values())
unallocated_budget = st.session_state.total_budget - allocated_budget
st.write(f"Allocated Budget: ${allocated_budget:.2f}")
st.write(f"Unallocated Budget: ${unallocated_budget:.2f}")


st.progress(total_expenses / st.session_state.total_budget if st.session_state.total_budget > 0 else 0)


st.header("Categories")
for category, budget in st.session_state.categories.items():
    category_expenses = sum(e['amount'] for e in st.session_state.expenses if e['category'] == category)
    remaining_category_budget = budget - category_expenses
    st.write(f"{category}: ${category_expenses:.2f} / ${budget:.2f} (Remaining: ${remaining_category_budget:.2f})")


st.header("Log Expense")
if list(st.session_state.categories.keys()):
    expense_category = st.selectbox("Select Category", list(st.session_state.categories.keys()))
    expense_amount = st.number_input("Expense Amount", value=0.0, step=5.0, min_value=0.0)
    expense_description = st.text_input("Expense Description")

    if st.button("Log Expense"):
        if expense_category and expense_amount > 0:
            category_budget = st.session_state.categories.get(expense_category, 0)
            category_expenses = sum(e['amount'] for e in st.session_state.expenses if e['category'] == expense_category)

            # Prevent expenses from exceeding category budget
            if category_expenses + expense_amount > category_budget:
                st.error(f"Expense exceeds budget for category '{expense_category}'.")
            # Prevent total expenses from exceeding total budget
            elif total_expenses + expense_amount > st.session_state.total_budget:
                st.error("This expense exceeds the total budget.")
            else:
                st.session_state.expenses.append({
                    "category": expense_category,
                    "amount": expense_amount,
                    "description": expense_description
                })
                st.experimental_rerun()
else:
    st.warning("Please add a category before logging an expense.")


st.header("Expenses")
for expense in st.session_state.expenses:
    st.write(f"- {expense['description']} ({expense['category']}): ${expense['amount']:.2f}")
