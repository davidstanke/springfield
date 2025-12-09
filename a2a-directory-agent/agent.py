from dotenv import load_dotenv
import os

from google.adk.a2a.utils.agent_to_a2a import to_a2a
from google.adk.agents import Agent
from toolbox_core import ToolboxSyncClient

load_dotenv()

# TOOLBOX_URL = os.getenv("TOOLBOX_URL", "http://127.0.0.1:5000")
TOOLBOX_URL = os.getenv("TOOLBOX_URL")
print(f"Connecting to toolbox at {TOOLBOX_URL}...")
client = ToolboxSyncClient(TOOLBOX_URL)

# Define your agent, including its capabilities/tools
root_agent = Agent(
    model='gemini-2.5-flash',
    name='hello_world_agent',
    description='An agent that can say hello and perform basic tasks.',
    instruction="You are a helpful AI assistant designed to provide accurate and useful information.",
    tools=client.load_toolset(),
)

# Make the agent A2A-compatible
A2A_PORT = os.getenv("A2A_PORT",8001)
a2a_app = to_a2a(root_agent, port=A2A_PORT)

# The to_a2a() function automatically generates the necessary FastAPI/Starlette app
# and the agent card (.well-known/agent-card.json) in memory.
