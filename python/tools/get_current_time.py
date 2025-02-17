from smolagents import Tool
from datetime import datetime
import pytz 

class GetCurrentTime(Tool):
    name = "get_current_time"
    description = "This is a tool that gets the current time for the specified timezone. Ask user for the timezone or location if not provided."
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
            current_time = datetime.now(tz)
            formatted_time = current_time.strftime("%H:%M:%S")
            return f"The current time in {timezone} is: {formatted_time}"
        
        except pytz.exceptions.UnknownTimeZoneError:
            return f"Invalid timezone: {timezone}. Please use a valid timezone identifier."
        
        except Exception as e:
            raise ValueError(f"Error getting time: {str(e)}")  