from tools.get_user_location import UserLocationTool
from tools.get_current_date import GetCurrentDate
from config import get_api_token

########################################################
# This script pushes tools to my HF hub.
########################################################

def push_tool_to_hub():
    # Initialize the tool
    user_location_tool = UserLocationTool()
    current_date_tool = GetCurrentDate() 
    
    # Push to hub
    user_location_tool.push_to_hub(
        repo_id="prige/User_Location_Tool",
        token=get_api_token(),
        private=False  # Set to True if you want a private repository
    )
    current_date_tool.push_to_hub(
        repo_id="prige/Current_Date_Tool",
        token=get_api_token(),
        private=False  # Set to True if you want a private repository
    )

if __name__ == "__main__":
    push_tool_to_hub() 