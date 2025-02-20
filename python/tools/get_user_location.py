from smolagents import Tool
import requests

class UserLocationTool(Tool):
    name = "get_user_location"
    description = "This tool returns the user's location based on their IP address"
    inputs = {}
    output_type = "string"
    
    def forward(self) -> str:
        try:
            response = requests.get("https://ipinfo.io/")
            data = response.json()
            return data["city"]
        except Exception as e:
            return f"Error getting user location: {str(e)}"