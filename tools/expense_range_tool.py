from smolagents import Tool
import pandas as pd
from datetime import datetime
import os

class ExpenseRangeTool(Tool):
    name = "expense_range"
    description = "Retrieve and analyze expenses between two dates"
    inputs = {
        "start_date": {
            "type": "string",
            "description": "Start date in YYYY-MM-DD format",
            "required": True
        },
        "end_date": {
            "type": "string",
            "description": "End date in YYYY-MM-DD format",
            "required": True
        }
    }
    output_type = "string"

    def __init__(self, csv_path="./expense_data.csv"):
        super().__init__()
        self.csv_path = csv_path
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"Expense data not found at {csv_path}")

    def forward(self, start_date: str, end_date: str) -> str:
        try:
            # Read the CSV file
            df = pd.read_csv(self.csv_path)
            
            # Convert dates to datetime
            df['Date'] = pd.to_datetime(df['Date'])
            start = pd.to_datetime(start_date)
            end = pd.to_datetime(end_date)
            
            # Filter by date range
            mask = (df['Date'] >= start) & (df['Date'] <= end)
            filtered_df = df[mask]
            
            if filtered_df.empty:
                return f"No expenses found between {start_date} and {end_date}"
            
            # Calculate summaries
            total_expenses = filtered_df[filtered_df['Amount'] < 0]['Amount'].sum()
            total_income = filtered_df[filtered_df['Amount'] > 0]['Amount'].sum()
            net_change = filtered_df['Amount'].sum()
            
            # Group by expense name for category breakdown
            category_summary = filtered_df[filtered_df['Amount'] < 0].groupby('Expense Name')['Amount'].sum()
            
            # Group by account
            account_summary = filtered_df.groupby('Account Number')['Amount'].sum()
            
            # Build response
            response = f"Expense Analysis ({start_date} to {end_date}):\n\n"
            
            response += "Summary:\n"
            response += f"Total Income: +${total_income:,.2f}\n"
            response += f"Total Expenses: ${total_expenses:,.2f}\n"
            response += f"Net Change: ${net_change:,.2f}\n\n"
            
            response += "Expense Breakdown by Category:\n"
            for category, amount in category_summary.items():
                response += f"{category}: ${amount:,.2f}\n"
            
            response += "\nAccount Balances:\n"
            for account, balance in account_summary.items():
                response += f"{account}: ${balance:,.2f}\n"
            
            response += "\nDetailed Transactions:\n"
            for _, row in filtered_df.iterrows():
                amount = row['Amount']
                sign = "+" if amount > 0 else ""
                response += (f"{row['Date'].strftime('%Y-%m-%d')}: {sign}${amount:,.2f} - "
                           f"{row['Expense Name']} ({row['Account Number']})\n")
            
            return response

        except Exception as e:
            raise ValueError(f"Error analyzing expenses: {str(e)}") 