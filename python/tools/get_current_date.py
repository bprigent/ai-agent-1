from smolagents import Tool
from datetime import datetime
import pytz

class GetCurrentDate(Tool):
    name = "get_current_date"
    description = "Gets the current date for the timezone provided"
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
            current_date = datetime.now(tz)
            formatted_date = current_date.strftime("%Y-%m-%d")
            return f"The current date in {timezone} is: {formatted_date}"
        
        except pytz.exceptions.UnknownTimeZoneError:
            return f"Invalid timezone: {timezone}. Please use a valid timezone identifier."
        
        except Exception as e:
            raise ValueError(f"Error getting datetime: {str(e)}")