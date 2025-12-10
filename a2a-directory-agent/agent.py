from dotenv import load_dotenv
import os

from google.adk.a2a.utils.agent_to_a2a import to_a2a
from google.adk.agents import Agent
from toolbox_core import ToolboxSyncClient
from a2a.types import AgentCard

load_dotenv()

client = ToolboxSyncClient(os.getenv("TOOLBOX_URL","TOOLBOX_URL_NOT_SET"))

agent_card = AgentCard(
    name="Simpsons directory agent",
    description="An agent to query a database of the residents of Springfield (from The Simpsons).",
    url=os.getenv("AGENT_URL","http://127.0.0.1:8001"),
    version="1.0.1",
    defaultInputModes=["text/plain"],
    defaultOutputModes=["text/plain"],
    capabilities={},
    skills=[
        {
            "description": "An agent that can work with a directory of Springfield residents. I am a helpful AI assistant designed to provide accurate and useful information about the residents of Springfield.",
            "id": "springfield_directory",
            "name": "model",
            "tags": ["llm"],
        },
        {
            "description": "Search residents by name\n\nArgs:\n first_name (str): The first name of the resident to search for",
            "id": "springfield_directory-search-users",
            "name": "search-users",
            "tags": ["llm", "tools"],
        },
    ],
)

# Define your agent, including its capabilities/tools
root_agent = Agent(
    model="gemini-2.5-flash",
    name="springfield_directory",
    description="An agent that can work with a directory of Springfield residents.",
    instruction="You are a helpful AI assistant designed to provide accurate and useful information about the residents of Springfield.",
    tools=client.load_toolset(),
)

# Make the agent A2A-compatible
a2a_app = to_a2a(root_agent, agent_card=agent_card)
