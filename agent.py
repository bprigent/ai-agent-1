from smolagents import CodeAgent, HfApiModel, DuckDuckGoSearchTool
from tools import CalculatorTool, DateTimeTool, ExpenseRangeTool, FinalAnswerTool



def main():
    # Initialize the model
    # You can use a default free model by not specifying model_id
    model = HfApiModel(
        max_tokens=2096,
        temperature=0.5,
        model_id='Qwen/Qwen2.5-Coder-32B-Instruct',
        custom_role_conversions=None,
    )
    
    # Get my tools
    calculator_tool = CalculatorTool()
    datetime_tool = DateTimeTool()
    expense_range_tool = ExpenseRangeTool()
    final_answer = FinalAnswerTool()
    search_the_internet = DuckDuckGoSearchTool()
    
    # Initialize the agent with the calculator tool
    agent = CodeAgent(
        tools=[calculator_tool, datetime_tool, expense_range_tool, final_answer, search_the_internet],
        model=model,
        add_base_tools=True,  # Add default toolbox
        verbosity_level=2  # Show detailed output of agent's thinking
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
