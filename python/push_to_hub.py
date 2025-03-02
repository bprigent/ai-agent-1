from config import get_api_token
from tools.get_user_location import UserLocationTool
from tools.get_current_date_and_time import GetCurrentDateAndTime
from tools.final_answer import FinalAnswerTool
from tools.user_input_tool import UserInputTool

########################################################
# This script pushes tools to my HF hub.
########################################################

def push_tool_to_hub():
    # Initialize the tool
    user_location_tool = UserLocationTool()
    current_date_tool = GetCurrentDateAndTime() 
    final_answer_tool = FinalAnswerTool()
    user_input_tool = UserInputTool()
    # Push to hub
    user_location_tool.push_to_hub(
        repo_id="prige/User_Location_Tool",
        token=get_api_token(),
        private=False  # Set to True if you want a private repository
    )
    current_date_tool.push_to_hub(
        repo_id="prige/Current_Date_And_Time_Tool",
        token=get_api_token(),
        private=False  # Set to True if you want a private repository
    )
    final_answer_tool.push_to_hub(
        repo_id="prige/Final_Answer_Tool",
        token=get_api_token(),
        private=False  # Set to True if you want a private repository
    )
    user_input_tool.push_to_hub(
        repo_id="prige/User_Input_Tool",
        token=get_api_token(),
        private=False  # Set to True if you want a private repository
    )

if __name__ == "__main__":
    push_tool_to_hub() 