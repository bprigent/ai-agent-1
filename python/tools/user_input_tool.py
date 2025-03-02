from smolagents import Tool

class UserInputTool(Tool):
    name = "user_input"
    description = "Asks for user's input on a specific question"
    inputs = {"question": {"type": "string", "description": "The question to ask the user"}}
    output_type = "string"
    
    def __init__(self):
        super().__init__()
        import logging
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.user_input = "" 
    
    async def _validate_question(self, question) -> tuple[bool, str]:
        # Helper method to validate the question
        if not isinstance(question, str):
            return False, f"Question must be a string, got {type(question)}"
        if not question.strip():
            return False, "Question cannot be empty"
        return True, question
    
    async def forward(self, question: str) -> str:
        # Validate the question first
        success, response = await self._validate_question(question)
        if not success:
            self.logger.error(response)
            return f"Error: {response}"
            
        # Ask the validated question and ensure non-empty response
        self.logger.info(f"Asking user: {question}")
        while True:
            self.user_input = input(f"{question} => Type your answer here:").strip()
            if self.user_input:
                break
            print("Please provide a non-empty answer.")
        
        self.logger.info(f"Received user input: {self.user_input}")
        return self.user_input