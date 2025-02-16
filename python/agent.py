from smolagents import CodeAgent, HfApiModel, DuckDuckGoSearchTool
from tools import CalculatorTool, DateTimeTool, ExpenseRangeTool, FinalAnswerTool
from python.config import get_api_token


def main():
    # Get the API token securely
    api_token = get_api_token()
    
    # Initialize the model with the token
    model = HfApiModel(
        max_tokens=2096, # Maximum number of tokens in the response
        temperature=0.5, # Temperature for the response
        model_id='Qwen/Qwen2.5-Coder-32B-Instruct', # Model ID
        custom_role_conversions=None, # Custom role conversions
        token=api_token  # Add the token here
    )


    # Get the tools for the models ready
    calculator_tool = CalculatorTool() # Calculator tool    
    datetime_tool = DateTimeTool() # DateTime tool
    expense_range_tool = ExpenseRangeTool() # Expense range tool
    final_answer = FinalAnswerTool() # Final answer tool
    search_the_internet = DuckDuckGoSearchTool() # Search the internet tool
    


    # Initialize the agent, the agent is a code agent
    agent = CodeAgent(
        tools=[calculator_tool, datetime_tool, expense_range_tool, final_answer, search_the_internet], # Tools
        model=model, # pass the model.
        add_base_tools=False, # we are not passing basic tools right now. In order to have better understanding of the agent abilities.
        verbosity_level=1,  # Show detailed output of agent's thinking.
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
