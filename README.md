# AI Agent Development Repository
Visit my [portfolio](www.bprigent.com)

This repository contains the implementation of AI agents following the Hugging Face [Building AI Agents course](https://huggingface.co/learn/agents-course/unit0/introduction). The project combines a Python backend for AI agent logic and a React frontend for user interaction. The goal of this project was to build a suite of tools both specific to the user need and also tools that any AI agent can use.

## Project set up
1. Clone the repository
2. Create a Venv. Important: you need to use python 3.10 because of smolagents.
3. Install the dependencies from the requirements.txt file.
4. Set up the react project and install the dependencies.
5. To run the project, you will need 3 terminals open. Terminal 1 will run the react project (cd react, npm start). Terminal 2 will run the python project (cd python, source venv/bin/activate, python run.py). Terminal 3 will run Phoenix to inspect the agent's actions (cd python, source venv/bin/activate, python -m phoenix.server.main serve)
6. Access the app. Go to [http://localhost:3000/](http://localhost:3000/) to see the app. Go to [http://localhost:6006/](http://localhost:6006/) to see the Phoenix interface.

## Project Structure
### Python Backend
#### API Layer (`api/main.py`)
- FastAPI implementation handling HTTP requests
- We have 3 main endpoints:
    - `/api/message-agent`: for agent interactions
    - `/api/fetch-all-expenses`: to get the expenses data
    - `/api/fetch-budget`: to get the budget data

In the `api/main.py` file, you can find the implementation of the agent and the tools. `model = HfApiModel()` is the model used to generate the agent's response. `agent = CodeAgent()` is the agent that is used to generate the response.

#### Tools Directory
I built 8 custom tools for this agent. They are quite simple and all use the class tool system. 
- Tools like `GetCurrentDateAndTime` or `UserLocationTool` are general purpose tools that can be used by any agent. 
- The `FinalAnswerTool` is here to make sure the agent always answers the user.
- Tools like `BudgetInfoTool` or `ExpenseListTool` are vertical specific tools that are used to answer questions about the user's budget or expenses.

#### Hugging Face Hub Integration
The `push_tool_to_hub.py` file is the way to push the tools to the Hugging Face Hub. I have made all the tools public and easily accessible through the Hub.

### React Frontend
#### Core Pages
- Home: Entry point and overview
- Budget: Financial management interface
- Additional feature-specific pages

#### State Management
Redux store implementation with the following slices:
- Agent slice: Manages AI agent state and interactions
- User slice: Handles user preferences and authentication
- Message slice: Controls chat history and message flow

#### Components
- `Navigation.js`: Main navigation structure
- `Header.js`: Application header with key controls
- Message Components:
  - `MessageList.js`: Displays conversation history
  - `MessageInput.js`: User input interface
  - `Message.js`: Individual message rendering

## Usage Examples
### Example 1: Financial Analysis
Example interaction:
User: "How much did I spend on food last month?"
Agent will process CSV data and provide detailed financial insights using the `get_current_date_and_time` tool and the tools related to budget analysis.

### Example 2: Budget Management
Example interaction:
User: "I need to know my monthly budget for groceries"
Agent will get the budget data using the tool called 'get_budget_data'.
