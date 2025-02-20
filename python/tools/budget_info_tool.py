from smolagents import Tool
import pandas as pd
import os

class BudgetInfoTool(Tool):
    name = "get_budget_info"
    description = "This is a tool that returns the categories of the budget and the amount for each category"
    inputs = {}
    output_type = "string"

    def __init__(self, csv_path="./data_budget.csv"):
        super().__init__()
        self.csv_path = csv_path
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"Budget data not found at {csv_path}")

    def forward(self) -> str:
        try:
            # Read the CSV file
            df = pd.read_csv(self.csv_path)
            title = "Budget Categories and Allocated Amounts for this user:\n"
            result = ""
            for _, row in df.iterrows():
                result += f"Allocated amount for the Budget Category called {row['Budget Category']} is {row['Budget Amount']}.\n"
            return title + result
        except Exception as e:
            raise ValueError(f"There was an error getting the budget info: {str(e)}")    