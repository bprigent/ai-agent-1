from transformers import pipeline, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("HuggingFaceTB/SmolLM2-1.7B-Instruct")

# this is to apply the chat template.
rendered_prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)



class SimpleAgent:
    def __init__(self):
        # Initialize a text generation pipeline
        self.generator = pipeline('text-generation', model='gpt2')
        
    def respond(self, prompt):
        """Generate a response based on the input prompt"""
        response = self.generator(prompt, max_length=100, num_return_sequences=1)
        return response[0]['generated_text']
    
    def run(self):
        """Run an interactive loop"""
        print("AI Agent initialized. Type 'quit' to exit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'quit':
                break
            
            response = self.respond(user_input)
            print(f"Agent: {response}")

if __name__ == "__main__":
    agent = SimpleAgent()
    agent.run()
