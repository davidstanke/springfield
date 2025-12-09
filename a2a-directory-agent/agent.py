from dotenv import load_dotenv
import os

from google.adk.a2a.utils.agent_to_a2a import to_a2a
from google.adk.agents import Agent

load_dotenv()

def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.

    Args:
        city (str): The name of the city for which to retrieve the weather report.

    Returns:
        dict: status and result or error msg.
    """
    if city.lower() == "new york":
        return {
            "status": "success",
            "report": (
                "The weather in New York is sunny with a temperature of 25 degrees"
                " Celsius (77 degrees Fahrenheit)."
            ),
        }
    else:
        return {
            "status": "error",
            "error_message": f"Weather information for '{city}' is not available.",
        }

# Define your agent, including its capabilities/tools
root_agent = Agent(
    model='gemini-2.5-flash',
    name='hello_world_agent',
    description='An agent that can say hello and perform basic tasks.',
    tools=[get_weather] 
)

# Make the agent A2A-compatible
a2a_app = to_a2a(root_agent, port=8001)

# The to_a2a() function automatically generates the necessary FastAPI/Starlette app
# and the agent card (.well-known/agent-card.json) in memory.
