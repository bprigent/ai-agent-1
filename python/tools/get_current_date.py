from smolagents import Tool


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

    def __init__(self, timezone: str = "UTC"):
        super().__init__()
        self.dependencies = ["pytz", "datetime"]
        self.timezone = timezone

    def forward(self, timezone: str) -> str:
        from datetime import datetime
        import pytz

        try:
            tz = pytz.timezone(timezone)
            current_date = datetime.now(tz)
            formatted_date = current_date.strftime("%Y-%m-%d")
            return f"The current date in {timezone} is: {formatted_date}"
        
        except pytz.exceptions.UnknownTimeZoneError:
            return f"Invalid timezone: {timezone}. Please use a valid timezone identifier."
        
        except Exception as e:
            raise ValueError(f"Error getting datetime: {str(e)}")