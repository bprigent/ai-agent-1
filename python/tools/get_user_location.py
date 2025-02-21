from smolagents import Tool

class UserLocationTool(Tool):
    name = "get_user_location"
    description = "This tool returns the user's location based on their IP address. That is all it does."
    inputs = {}
    output_type = "string"
    
    def __init__(self):
        super().__init__()
        self.dependencies = ["requests"]
    
    def forward(self) -> str:
        import requests
        
        try:
            response = requests.get("https://ipinfo.io/")
            data = response.json()
            return f"According to your IP address, the user's location is {data['city']}, {data['region']}, {data['country']}."
        
        except Exception as e:
            return f"Error getting user location: {str(e)}. It looks like https://ipinfo.io/ did not return a valid response."
        