from smolagents import Tool
from typing import Any

class UserLocationTool(Tool):
    name = "get_user_location"
    description = "This tool returns the user's location based on their IP address. That is all it does."
    inputs = {}
    output_type = "string"
    
    def __init__(self): # Initialize the logger
        super().__init__()
        import logging
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
    
    def _validate_location_data(self, response: Any) -> tuple[bool, str]:
        # Validates the API response, JSON parsing, and location data. Returns (is_valid, error_message or location_string)
        import json
        
        if response.status != 200: # Check HTTP status
            if response.status == 429:
                return False, "Rate limit exceeded for IP geolocation service. Please try again later."
            return False, f"Server returned HTTP {response.status}"
            
        try: # Parse and validate JSON
            response_data = response.json()
        except json.JSONDecodeError:
            return False, "Invalid response from server"
            
        if not isinstance(response_data, dict): # Validate response data type
            return False, f"Expected dictionary data, got {type(response_data)}"
            
        required_fields = ['city', 'region', 'country'] # Validate required fields
        missing_fields = [field for field in required_fields if not response_data.get(field)]
        if missing_fields:
            return False, f"Missing or empty location fields: {', '.join(missing_fields)}"
            
        location = f"According to your IP address, the user's location is {response_data['city']}, {response_data['region']}, {response_data['country']}."
        return True, location
    
    async def _call_api(self) -> tuple[bool, Any]:
        # Makes the API call to ipinfo.io. Returns (success, response_object_or_error_message)
        import aiohttp
        import asyncio
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://ipinfo.io/", timeout=5) as response:
                    return True, response
        except asyncio.TimeoutError:
            return False, "Request timed out after 5 seconds. Please try again."
        except aiohttp.ClientError as e:
            return False, "Unable to connect to location service. Please check your internet connection."
        except Exception as e:
            return False, f"An unexpected error occurred: {str(e)}"

    async def forward(self) -> str:
        # Send the request to the API
        success, response = await self._call_api()
        if not success:
            self.logger.error(response)
            return f"Error getting user location: {response}"
        
        # Validate response format
        is_valid, result = self._validate_location_data(response)
        if not is_valid:
            self.logger.error(f"Data validation failed: {result}")
            return f"Error getting user location: {result}"
        
        self.logger.info(f"Successfully retrieved location: {result}")
        return result
        
