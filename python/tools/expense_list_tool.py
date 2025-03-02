from smolagents import Tool
import pandas as pd
import os

class ExpenseListTool(Tool):
    name = "get_list_of_expenses"
    description = "This tool returns the raw list of expenses between two dates, it does not provide summaries"
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

    def __init__(self, csv_path="./data_expenses.csv"):
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
                return f"No expenses were found between between {start_date} and {end_date}. The user did not spend any money in this time period."
            
            # Sort by date
            filtered_df = filtered_df.sort_values('Date')

            result = ""
            for _, row in filtered_df.iterrows():
                result += f"Date: {row['Date']}, Expense Name: {row['Expense Name']}, Amount: {abs(row['Amount']):,.2f}, Account Number: {row['Account Number']}, Budget Category: {row['Budget Category']}.\n"

            return result

        except Exception as e:
            raise ValueError(f"Error listing expenses: {str(e)}") 