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
    name='hello_world_agent',
    description='An agent that can say hello and perform basic tasks.',
    instruction="You are a helpful AI assistant designed to provide accurate and useful information.",
    tools=client.load_toolset(),
)

# # Define A2A agent card
# my_agent_card = AgentCard(
#     name="file_agent",
#     url=A2A_HOST,
#     description="An agent that can offer information about residents of Springfield",
#     version="1.0.0",
#     capabilities={},
#     skills= [
#             {
#             "description": "An agent that can say hello and perform basic tasks. I am a helpful AI assistant designed to provide accurate and useful information about the residents of Springfield.",
#             "id": "hello_world_agent",
#             "name": "model",
#             "tags": [
#                 "llm"
#             ]
#             },
#             {
#             "description": "Search residents by name\n\nArgs:\n    first_name (str): The first name of the resident to search for",
#             "id": "hello_world_agent-search-users",
#             "name": "search-users",
#             "tags": [
#                 "llm",
#                 "tools"
#             ]
#             }
#         ],
#     defaultInputModes= ["text/plain"],
#     defaultOutputModes= ["text/plain"],
#     supportsAuthenticatedExtendedCard=False,
# )

# Make the agent A2A-compatible
a2a_app = to_a2a(root_agent, port=A2A_PORT, host=A2A_HOST)
# a2a_app = to_a2a(root_agent, port=A2A_PORT, agent_card=my_agent_card)

# The to_a2a() function automatically generates the necessary FastAPI/Starlette app
# and the agent card (.well-known/agent-card.json) in memory.
