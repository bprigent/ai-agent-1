from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from pydantic import BaseModel
import os
from agent import CodeAgent, HfApiModel, DuckDuckGoSearchTool
from tools import (
    GetCurrentDateAndTime,
    FinalAnswerTool,
    ExpenseListTool,
    ExpenseSummaryTool,
    BudgetInfoTool,
    UserInputTool,
    ComputeAvailableCash,
    UserLocationTool
)
from config import get_api_token
from phoenix.otel import register
from openinference.instrumentation.smolagents import SmolagentsInstrumentor 

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React app address
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register()
SmolagentsInstrumentor().instrument() # go to http://0.0.0.0:6006/ to see the logs


# Initialize agent
api_token = get_api_token()
model = HfApiModel(
    max_tokens=10000,
    temperature=0.5,
    model_id='Qwen/Qwen2.5-Coder-32B-Instruct',
    custom_role_conversions=None,
    token=api_token
)

# Initialize tools
date_and_time_tool = GetCurrentDateAndTime()
expense_list = ExpenseListTool()
expense_summary = ExpenseSummaryTool()
final_answer = FinalAnswerTool()
budget_info = BudgetInfoTool()
user_input = UserInputTool()
web_search = DuckDuckGoSearchTool()
compute_available_cash = ComputeAvailableCash()
user_location = UserLocationTool()

# Initialize the agent
agent = CodeAgent(
    tools=[
        date_and_time_tool,
        expense_list,
        expense_summary,
        final_answer,
        budget_info,
        user_input,
        web_search,
        compute_available_cash,
        user_location
    ],
    model=model,
    add_base_tools=False,
    verbosity_level=2
)
additional_instructions = '''
 You are an expert in all things finance. You are able to answer questions about the user's finances and help them with their finances.
 You answer is short and concise sentences, for example, you never simply answer with a number, you always explain what the number is and what it means.
'''
agent.prompt_templates["system_prompt"] = agent.prompt_templates["system_prompt"] + additional_instructions


########################################################
# API ENDPOINTS
########################################################
class AgentMessage(BaseModel):
    message: str

@app.post("/api/message-agent")
async def message_agent(message: AgentMessage):
    try:
        print(f"Received message: {message.message}")  # Add logging
        result = agent.run(
            message.message, 
            reset=False # This is to prevent the agent from resetting the memory. It will remember the previous messages.
        )
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