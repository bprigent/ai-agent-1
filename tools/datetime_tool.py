from smolagents import Tool
from datetime import datetime

class DateTimeTool(Tool):
    name = "get_current_time"
    description = "Gets the current date and time in a specified format"
    inputs = {
        "format": {
            "type": "string",
            "description": "Format string for datetime (e.g., '%H:%M:%S' for time only, '%Y-%m-%d %H:%M:%S' for date and time)",
            "nullable": True,
            "default": "%Y-%m-%d %H:%M:%S"
        }
    }
    output_type = "string"

    def forward(self, format: str = "%Y-%m-%d %H:%M:%S") -> str:
        try:
            current_time = datetime.now().strftime(format)
            return current_time
        except Exception as e:
            raise ValueError(f"Error formatting datetime: {str(e)}") 