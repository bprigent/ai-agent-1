# AI Agent Development Repository
Visit my [portfolio](https://www.bprigent.com)

PROJECT STATUS: COMPLETE (as of 03/02/2025)

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
I created 5 main pages. The goal of building all these useless pages was to practice using react router.
- Home: Entry point and overview
- Budget: Financial management interface
- Expenses: Expense management interface
- Chat: Chat interface, this is where the agent is used.
- 404: 404 page (not found)

#### Components
In order to make my code more manageable, I created a components folder where I placed the reusable components. 
- `Navigation.js`: Main navigation structure
- `Header.js`: Application header with key controls
- Message Components:
  - `MessageList.js`: Displays conversation history
  - `MessageInput.js`: User input interface
  - `Message.js`: Individual message rendering
- Table Components:
  - `TableRows.js`: Reusable table rows component
  - `TableHeaders.js`: Reusable table headers component

#### Styling
I used the Material-UI library to style the app. You can see the theme in `App.js`.

#### Data management in the frontend
I used the Redux store to manage the data in the frontend. You can find the slices in the `store` folder. You've got 3 slices:
- Agent slice: Manages the messages between the AI and the user.
- Expenses slice: Manages the expenses data. The main feature here is to fetch the expenses data from the backend and to display it in the `Expenses` page.
- Budget slice: Manages the budget data. Similarly, the feature is to fetch the budget data from the backend and to display it in the `Budget` page.

## Usage Examples
### Example 1: Financial Analysis
Example interaction:
User: "How much did I spend on food last month?"
Agent will process CSV data and provide detailed financial insights using the `get_current_date_and_time` tool and the tools related to budget analysis.

### Example 2: Budget Management
Example interaction:
User: "I need to know my monthly budget for groceries"
Agent will get the budget data using the tool called 'get_budget_data'.
