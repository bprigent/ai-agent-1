from smolagents import Tool
from datetime import datetime

class DateTimeTool(Tool):
    name = "datetime"
    description = "Get current date and time information"
    inputs = {
        "format": {
            "type": "string",
            "description": "Format string for datetime (optional)",
            "nullable": True,
            "default": "%Y-%m-%d %H:%M:%S"
        }
    }
    output_type = "string"

    def forward(self, format: str = "%Y-%m-%d %H:%M:%S") -> str:
        try:
            return datetime.now().strftime(format)
        except Exception as e:
            raise ValueError(f"Error formatting datetime: {str(e)}") 