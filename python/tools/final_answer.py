from typing import Any, Optional
from smolagents import Tool

class FinalAnswerTool(Tool):
    name = "final_answer"
    description = "This is a tool sends the final answer to the given problem, towards the user. This tool does not format the answer, it just sends it as is."
    inputs = {'answer': {'type': 'any', 'description': 'The well formated, short, and conversational final answer to the user`s problem (or request).'}}
    output_type = "any"

    def forward(self, answer: Any) -> Any:
        return answer

    def __init__(self, *args, **kwargs):
        self.is_initialized = False