from smolagents import Tool
from datetime import datetime
import pytz

class DateTimeTool(Tool):
    name = "get_current_time"
    description = "Gets the current date and time in a specified format"
    inputs = {
        "timezone": {
            "type": "string",
            "description": "Optional timezone (e.g., 'UTC', 'US/Pacific', 'Europe/London'). Defaults to UTC",
            "required": False,
            "nullable": True
        }
    }
    output_type = "string"

    def forward(self, timezone: str = "UTC") -> str:
        try:
            tz = pytz.timezone(timezone)
            current_time = datetime.now(tz)
            formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S %Z")
            return f"The current local time in {timezone} is: {formatted_time}"
        except pytz.exceptions.UnknownTimeZoneError:
            return f"Invalid timezone: {timezone}. Please use a valid timezone identifier."
        except Exception as e:
            raise ValueError(f"Error getting datetime: {str(e)}") 