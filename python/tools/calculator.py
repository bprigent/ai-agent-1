from smolagents import Tool

class CalculatorTool(Tool):
    name = "calculator"
    description = "A basic calculator that can perform arithmetic operations (+, -, *, /)"
    inputs = {
        "expression": {
            "type": "string",
            "description": "The arithmetic expression to evaluate (e.g. '2 + 3', '10 * 5')"
        }
    }
    output_type = "string"

    def forward(self, expression: str) -> str:
        try:
            allowed_chars = set('0123456789+-*/ .()')
            if not all(c in allowed_chars for c in expression):
                raise ValueError("Invalid characters in expression")
            
            result = eval(expression, {"__builtins__": {}}, {})
            return str(result)
        except Exception as e:
            raise ValueError(f"Error evaluating expression: {str(e)}")