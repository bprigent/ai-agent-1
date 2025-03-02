from smolagents import Tool
import pandas as pd
import os

class ComputeAvailableCash(Tool):
    name = "compute_available_cash"
    description = (
        '''Estimates available cash for savings or investing at the end of the month by comparing
        budgeted amounts per category with actual expenses. For each category, it calculates the amount underspent
        or overspent, it then summarizes the total final budget, and determines if there is money to allocate to savings or investing.'''
    )
    inputs = {
        "month": {
            "type": "integer",
            "description": "the number of the month (between 1 and 12) for which to estimate savings",
            "required": True
        },
        "year": {
            "type": "integer",
            "description": "the year (e.g., 2023) for which to estimate savings",
            "required": True
        }
    }
    output_type = "string"

    def __init__(self, expenses_csv_path="./data_expenses.csv", budget_csv_path="./data_budget.csv"):
        super().__init__()
        self.expenses_csv_path = expenses_csv_path
        self.budget_csv_path = budget_csv_path
        if not os.path.exists(expenses_csv_path):
            raise FileNotFoundError(f"Expense data not found at {expenses_csv_path}")
        if not os.path.exists(budget_csv_path):
            raise FileNotFoundError(f"Budget data not found at {budget_csv_path}")
    
    def forward(self, month: int, year: int) -> str:
        # Load budget data
        try:
            budget_df = pd.read_csv(self.budget_csv_path)
        except Exception as e:
            raise ValueError(f"Error reading budget CSV: {str(e)}")
        
        # budget_df has columns: 'Budget Category' and 'BudgetAmount'
        # create a dictionary with the budget amounts for each category
        budget_dict = {}
        for _, row in budget_df.iterrows():
            category = row["Budget Category"]
            # Skip Salary and Savings categories
            if category not in ['Salary', 'Savings']:
                amount = row["Budget Amount"]
                budget_dict[category] = amount

        # Load expenses data and filter by month and year
        try:
            expenses_df = pd.read_csv(self.expenses_csv_path)
            expenses_df["Date"] = pd.to_datetime(expenses_df["Date"])
            # Convert expenses to absolute values
            expenses_df["Amount"] = expenses_df["Amount"].abs()
        except Exception as e:
            raise ValueError(f"Error reading expenses CSV: {str(e)}")
            
        filtered_expenses = expenses_df[
            (expenses_df["Date"].dt.month == month) & 
            (expenses_df["Date"].dt.year == year)
        ]
        if filtered_expenses.empty:
            return f"No expenses found for {month}/{year}. It seems the user did not spend any money in that period."

        # Calculate total expenses for each Budget Category
        expenses_by_category = filtered_expenses.groupby("Budget Category")["Amount"].sum()

        # Compare budget vs. actual expenses for each category
        details = "Budget vs. Actual Expenses:\n"
        total_budget = sum(budget_dict.values())  # Sum of all budget amounts
        total_spent = 0

        # iterate over the budget categories and compare the budget amount with the actual expenses
        for category, budget_amount in budget_dict.items():
            # Skip Salary and Savings categories
            if category in ['Salary', 'Savings']:
                continue
                
            # get the actual expenses for the category
            actual_expense = expenses_by_category.get(category, 0)
            total_spent += actual_expense  # Add to total spent
            
            # Compare budget vs actual
            if actual_expense > budget_amount:
                details += f"{category}: Budgeted ${budget_amount:,.2f}, Spent ${actual_expense:,.2f} (Overspent by ${actual_expense - budget_amount:,.2f})\n"
            else:
                details += f"{category}: Budgeted ${budget_amount:,.2f}, Spent ${actual_expense:,.2f} (Underspent by ${budget_amount - actual_expense:,.2f})\n"

        # Calculate available savings (positive means under budget)
        available_savings = total_budget - total_spent
        
        final_summary = (
            "\nTOTAL SUMMARY:\n" + "-" * 30 + "\n"
            f"Total Budget: ${total_budget:,.2f}\n"
            f"Total Spent: ${total_spent:,.2f}\n"
            f"Net Difference: ${total_budget - total_spent:,.2f}\n"
            f"Available for Savings/Investing: ${max(0, available_savings):,.2f}\n"
        )

        return f"{details}\n{final_summary}"
        
        
        