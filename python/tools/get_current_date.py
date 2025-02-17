from smolagents import Tool
from datetime import datetime
import pytz

class GetCurrentDate(Tool):
    name = "get_current_date"
    description = "This is a tool that gets the current date for the specified timezone. Ask user for the timezone or location if not provided."
    inputs = { 
        "timezone": {
            "type": "string",
            "description": "Timezone (e.g., 'UTC', 'US/Pacific', 'Europe/London')",
            "required": True
        }
    }
    output_type = "string"

    def forward(self, timezone: str) -> str:
        try:
            tz = pytz.timezone(timezone)
            current_date = datetime.now(tz)
            formatted_date = current_date.strftime("%Y-%m-%d")
            return f"The current date in {timezone} is: {formatted_date}"
        
        except pytz.exceptions.UnknownTimeZoneError:
            return f"Invalid timezone: {timezone}. Please use a valid timezone identifier."
        
        except Exception as e:
            raise ValueError(f"Error getting datetime: {str(e)}")