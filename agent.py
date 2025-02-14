from smolagents import CodeAgent, HfApiModel, Tool



# Create a simple calculator tool
class CalculatorTool(Tool):
    name = "calculator"
    description = "A basic calculator that can perform arithmetic operations (+, -, *, /)"
    inputs = {
        "expression": {
            "type": "string",
            "description": "The arithmetic expression to evaluate (e.g. '2 + 3', '10 * 5')"
        }
    }
    output_type = "float"

    def forward(self, expression: str) -> float:
        try:
            # Safely evaluate basic arithmetic expressions
            allowed_chars = set('0123456789+-*/ .()')
            if not all(c in allowed_chars for c in expression):
                raise ValueError("Invalid characters in expression")
            
            result = eval(expression, {"__builtins__": {}}, {})
            return float(result)
        except Exception as e:
            raise ValueError(f"Error evaluating expression: {str(e)}")




def main():
    # Initialize the model
    # You can use a default free model by not specifying model_id
    model = HfApiModel()
    
    # Create calculator tool instance
    calculator_tool = CalculatorTool()
    
    # Initialize the agent with the calculator tool
    agent = CodeAgent(
        tools=[calculator_tool],
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
