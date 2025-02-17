from smolagents import CodeAgent, HfApiModel, DuckDuckGoSearchTool, PythonInterpreterTool
from tools import GetCurrentDate, FinalAnswerTool, GetCurrentTime, ExpenseListTool, ExpenseSummaryTool, BudgetInfoTool, UserInputTool
from config import get_api_token



def main():
    # Get the API token securely
    api_token = get_api_token()
    
    # Initialize the model with the token
    model = HfApiModel(
        max_tokens=10000, # Maximum number of tokens in the response
        temperature=0.5, # Temperature for the response
        model_id='Qwen/Qwen2.5-Coder-32B-Instruct', # Model ID
        custom_role_conversions=None, # Custom role conversions
        token=api_token  # Add the token here
    )


    # Get the tools for the models ready
    date_tool = GetCurrentDate() # DateTime tool
    time_tool = GetCurrentTime() # DateTime tool
    expense_list = ExpenseListTool() # Expense list tool
    expense_summary = ExpenseSummaryTool() # Expense summary tool
    final_answer = FinalAnswerTool() # Final answer tool
    search_the_internet = DuckDuckGoSearchTool() # Search the internet tool
    python_interpreter = PythonInterpreterTool() # Python interpreter tool
    budget_info = BudgetInfoTool() # Budget info tool
    user_input = UserInputTool() # User input tool

    # Initialize the agent, the agent is a code agent
    agent = CodeAgent(
        tools=[
            date_tool, 
            time_tool,
            expense_list, 
            expense_summary, 
            final_answer, 
            search_the_internet, 
            python_interpreter,
            budget_info,
            user_input
        ], # Tools
        model=model, # pass the model.
        add_base_tools=False, # we are not passing basic tools right now. In order to have better understanding of the agent abilities.
        verbosity_level=2,  # How much detail to show in the output
        additional_authorized_imports=[] # Additional authorized imports modules can be added here.
    )
    


    # Print that things are ready
    print("AI Agent initialized. Type 'quit' to exit.")
    



    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
            
        try:
            result = agent.run(user_input)
            print(f"Agent: {result}")
            
        except Exception as e:
            print(f"Error: {str(e)}")




if __name__ == "__main__":
    main()
