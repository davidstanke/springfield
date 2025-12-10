from dotenv import load_dotenv
import os

from google.adk.a2a.utils.agent_to_a2a import to_a2a
from google.adk.agents import Agent
from toolbox_core import ToolboxSyncClient
from a2a.types import AgentCard

load_dotenv()

A2A_PORT = os.getenv("A2A_PORT",8001)
A2A_HOST = os.getenv("HOST_OVERRIDE",f"localhost:{A2A_PORT}")

# TOOLBOX_URL = os.getenv("TOOLBOX_URL", "http://127.0.0.1:5000")
TOOLBOX_URL = os.getenv("TOOLBOX_URL")
print(f"Connecting to toolbox at {TOOLBOX_URL}...")
client = ToolboxSyncClient(TOOLBOX_URL)

# Define your agent, including its capabilities/tools
root_agent = Agent(
    model='gemini-2.5-flash',
    name='springfield_directory',
    description='An agent that can work with a directory of Springfield residents.',
    instruction="You are a helpful AI assistant designed to provide accurate and useful information about the residents of Springfield.",
    tools=client.load_toolset(),
)

# Make the agent A2A-compatible
a2a_app = to_a2a(root_agent, port=A2A_PORT, host=A2A_HOST)
# a2a_app = to_a2a(root_agent, port=A2A_PORT, agent_card=my_agent_card)

# The to_a2a() function automatically generates the necessary FastAPI/Starlette app
# and the agent card (.well-known/agent-card.json) in memory.
