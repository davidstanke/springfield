from dotenv import load_dotenv
import os

from google.adk.a2a.utils.agent_to_a2a import to_a2a
from google.adk.agents import Agent
from toolbox_core import ToolboxSyncClient
from a2a.types import AgentCard

load_dotenv()

agent_host = os.getenv("AGENT_HOST", "localhost")
agent_port = os.getenv("AGENT_PORT", 8000)
agent_protocol = os.getenv("AGENT_PROTOCOL", "http")

client = ToolboxSyncClient(os.getenv("TOOLBOX_URL", "TOOLBOX_URL_NOT_SET"))

def get_weather_dummy_tool(city: str, unit: str):
    """
    Retrieves the weather for a city in the specified unit.

    Args:
        city (str): The city name.
        unit (str): The temperature unit, either 'Celsius' or 'Fahrenheit'.
    """
    # ... function logic ...
    return {"status": "success", "report": f"Weather for {city} is sunny."}

# Define your agent, including its capabilities/tools
root_agent = Agent(
    model="gemini-2.5-flash",
    name="springfield_directory",
    description="An agent that can work with a directory of Springfield residents.",
    instruction="You are a helpful AI assistant designed to provide accurate and useful information about the residents of Springfield.",
    tools=client.load_toolset() + [get_weather_dummy_tool],
)

# Make the agent A2A-compatible
# a2a_app = to_a2a(root_agent, agent_card=agent_card)
a2a_app = to_a2a(root_agent, host=agent_host, port=agent_port, protocol=agent_protocol)
