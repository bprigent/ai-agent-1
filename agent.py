from smolagents import CodeAgent, HfApiModel
from tools import CalculatorTool, DateTimeTool, ExpenseRangeTool



def main():
    # Initialize the model
    # You can use a default free model by not specifying model_id
    model = HfApiModel()
    
    # Create calculator tool instance
    calculator_tool = CalculatorTool()
    datetime_tool = DateTimeTool()
    expense_range_tool = ExpenseRangeTool()
    
    # Initialize the agent with the calculator tool
    agent = CodeAgent(
        tools=[calculator_tool, datetime_tool, expense_range_tool],
        model=model,
        add_base_tools=True,  # Add default toolbox
        verbosity_level=2  # Show detailed output of agent's thinking
    )
    
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
