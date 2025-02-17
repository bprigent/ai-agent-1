from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from pydantic import BaseModel
import os
from agent import CodeAgent, HfApiModel, DuckDuckGoSearchTool # Import the agent components
from tools import GetCurrentDate, FinalAnswerTool, GetCurrentTime, ExpenseListTool, ExpenseSummaryTool, BudgetInfoTool, UserInputTool
from config import get_api_token

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React app address
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Expense(BaseModel):
    date: str
    expense_name: str
    amount: float
    account_number: str
    budget_category: str

class AgentMessage(BaseModel):
    message: str

# Initialize agent (moved outside endpoint for persistence)
api_token = get_api_token()
model = HfApiModel(
    max_tokens=10000,
    temperature=0.5,
    model_id='Qwen/Qwen2.5-Coder-32B-Instruct',
    custom_role_conversions=None,
    token=api_token
)

# Initialize tools
date_tool = GetCurrentDate()
time_tool = GetCurrentTime()
expense_list = ExpenseListTool()
expense_summary = ExpenseSummaryTool()
final_answer = FinalAnswerTool()
budget_info = BudgetInfoTool()
user_input = UserInputTool()
web_search = DuckDuckGoSearchTool()

# Initialize the agent
agent = CodeAgent(
    tools=[
        date_tool,
        time_tool,
        expense_list,
        expense_summary,
        final_answer,
        budget_info,
        user_input,
        web_search
    ],
    model=model,
    add_base_tools=False,
    verbosity_level=2,
)

########################################################
# API ENDPOINTS
########################################################
@app.get("/api/fetch-all-expenses")
async def get_expenses():
    # Get the correct path to the CSV file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(os.path.dirname(current_dir), "data_expenses.csv")
    
    # Read the CSV file
    df = pd.read_csv(csv_path)
    
    # Convert dates to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Sort by date
    df = df.sort_values('Date')
    
    # Convert to list of dictionaries
    expenses = df.to_dict('records')
    
    return {
        "expenses": expenses
    }

@app.get("/api/fetch-budget")
async def get_budget():
    # Get the correct path to the CSV file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(os.path.dirname(current_dir), "data_budget.csv")
    
    # Read the CSV file
    df = pd.read_csv(csv_path)
    
    # Convert to list of dictionaries
    budget = df.to_dict('records')
    
    return {
        "budget": budget
    }

@app.post("/api/message-agent")
async def message_agent(message: AgentMessage):
    try:
        print(f"Received message: {message.message}")  # Add logging
        result = agent.run(message.message)
        print(f"Agent response: {result}")  # Add logging
        return {
            "response": result,
            "status": "success"
        }
    except Exception as e:
        print(f"Error in message_agent: {str(e)}")  # Add error logging
        return {
            "response": str(e),
            "status": "error"
        }