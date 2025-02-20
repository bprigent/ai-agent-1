from smolagents import Tool
import pandas as pd
import os

class ExpenseSummaryTool(Tool):
    name = "get_sum_of_expenses"
    description = "This tool returns the sum (or total) of expenses between two dates, this will be grouped by budget category, separated into costs and revenue"
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
                return f"No expenses found between {start_date} and {end_date}. Therefore, there is no summary to provide for this time period and user."
            
            # Split into costs and revenue
            costs_df = filtered_df[filtered_df['Amount'] < 0]
            revenue_df = filtered_df[filtered_df['Amount'] > 0]
            
            # Build response
            response = f"Expense summary for the period between {start_date} and {end_date}:\n\n"
            
            # Add budget category summaries
            response += "SUMMARY BY BUDGET CATEGORY:\n"
            response += "Costs (cash out) categories:\n"
            category_costs = costs_df.groupby('Budget Category')['Amount'].sum().sort_values()
            for category, amount in category_costs.items():
                response += f"${abs(amount):,.2f} spent on {category}.\n"
            
            response += "\nRevenue (cash in) categories:\n"
            category_revenue = revenue_df.groupby('Budget Category')['Amount'].sum().sort_values(ascending=False)
            for category, amount in category_revenue.items():
                response += f"${abs(amount):,.2f} earned from {category}.\n"
            
            # Add total summary
            total_costs = costs_df['Amount'].sum()
            total_revenue = revenue_df['Amount'].sum()
            net_amount = total_revenue + total_costs  # total_costs is negative
            
            response += f"\nTOTAL SUMMARY:\n"
            response += f"Total Costs: ${abs(total_costs):,.2f}\n"
            response += f"Total Revenue: ${total_revenue:,.2f}\n"
            response += f"Net Amount: ${net_amount:,.2f}\n"
            
            return response

        except Exception as e:
            raise ValueError(f"Error summarizing expenses: {str(e)}") 