from smolagents import Tool
from typing import Any

class GetCurrentDateAndTime(Tool):
    name = "get_current_date_and_time"
    description = "This is a tool that gets the current date, day of the week, and time for the specified timezone. Ask user for the timezone or location if not provided."
    inputs = {
        "timezone": {
            "type": "string",
            "description": "Timezone (e.g., 'UTC', 'US/Pacific', 'Europe/London')",
            "required": True
        }
    }
    output_type = "string"

    def _validate_timezone(self, timezone: str) -> Any:
        # Validate and return a timezone object. Returns None if timezone is invalid.
        import pytz
        
        if not isinstance(timezone, str):
            raise ValueError("Timezone must be a string")
        
        if not timezone.strip():
            raise ValueError("Timezone cannot be empty")

        try:
            return pytz.timezone(timezone)
        except pytz.exceptions.UnknownTimeZoneError:
            suggested_timezones = [
                tz for tz in pytz.all_timezones 
                if timezone.lower() in tz.lower()
            ][:3]
            error_msg = f"Invalid timezone: '{timezone}'"
            if suggested_timezones:
                error_msg += f". Did you mean one of these? {', '.join(suggested_timezones)}"
            else:
                error_msg += ". Please use a valid timezone identifier from the IANA Time Zone Database"
            raise ValueError(error_msg)
    
    def _format_answer(self, timezone, current_datetime) -> str:
        # Format the answer
        formatted_date = current_datetime.strftime("%Y-%m-%d")
        formatted_time = current_datetime.strftime("%H:%M:%S")
        day_of_week = current_datetime.strftime("%A")
        return f"In {timezone}, it is {day_of_week}, {formatted_date} at {formatted_time}"

    def forward(self, timezone: str) -> str:
        # Forward function
        from datetime import datetime
        
        try:
            tz = self._validate_timezone(timezone)
            current_datetime = datetime.now(tz)
            return self._format_answer(timezone, current_datetime)
        
        except ValueError as ve: # Re-raise ValueError with the detailed message
            raise ValueError(str(ve))
        
        except Exception as e: # Handle any unexpected errors
            raise ValueError(f"Unexpected error getting date and time: {str(e)}")