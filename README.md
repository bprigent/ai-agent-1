# AI Agent Development Repository
Visit my [portfolio](www.bprigent.com)

This repository contains the implementation of AI agents following the Hugging Face [Building AI Agents course](https://huggingface.co/learn/agents-course/unit0/introduction). The project combines a Python backend for AI agent logic and a React frontend for user interaction. The goal of this project was to build a suite of tools both specific to the user need and also tools that any AI agent can use.

## Project set up
1. Clone the repository
2. Create a Venv. Immportant: you need to use python 3.10 because of smolagents.
3. Install the dependencies from the requirements.txt file.
4. Set up the react project and install the dependencies.
5. To run the project, you will need 3 terminals open. Terminal 1 will run the react project (cd react, npm start). Terminal 2 will run the python project (cd python, source venv/bin/activate, python run.py). Terminal 3 will run Phoenix to inspect the agent's actions (cd python, source venv/bin/activate, python -m phoenix.server.main serve)
6. Access the app. Go to [http://localhost:3000/](http://localhost:3000/) to see the app. Go to [http://localhost:6006/](http://localhost:6006/) to see the Phoenix interface.

## Project Structure
### Python Backend
#### API Layer (`api/main.py`)
- FastAPI implementation handling HTTP requests
- Endpoints for agent interactions and data management
- WebSocket support for real-time communication

#### Agent Components
- `agent.py`: Core agent implementation using the ReAct (Reasoning and Acting) framework
- `config.py`: Configuration settings for the agent, including model parameters and API keys
- CSV files used as a lightweight database for development purposes

#### Tools Directory
Custom tools and utilities for the agent:
- `final_answer.py`: Processes and formats agent's final responses
- Additional specialized tools for specific agent capabilities

#### Hugging Face Integration
- Push to Hub functionality for model sharing and version control
- Easy deployment and collaboration through Hugging Face's infrastructure

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
