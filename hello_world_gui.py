import taipy as tp

from taipy import Gui
from taipy import Config
from taipy import Core

# Configure application


def build_message(name: str)-> str:
    return f"Received message :  {name}"

# A first data node configuration to model an input name.
input_name_data_node_cfg = Config.configure_data_node(id="input_name")
# A second data node configuration to model the message to display
message_data_node_cfg = Config.configure_data_node(id="message")
# Configure task between input and output data nodes
build_msg_task_cfg = Config.configure_task("build_msg", build_message, input_name_data_node_cfg,message_data_node_cfg)
# Scenario Configuration to represent execution graph
scenario_cfg = Config.configure_scenario("scenario", task_configs=[build_msg_task_cfg])

# Function to handle state from GUI
input_name = "Taipy"
message = None

def submit_scenario(state):
    state.scenario.input_name.write(state.input_name)
    state.scenario.submit()
    state.message = scenario.message.read()

# Markdown representation of the user interface
page = """
Name: <|{input_name}|input|>
<|submit|button|on_action=submit_scenario|>

Message: <|{message}|text|>
"""

if __name__ == "__main__":
    # Instantiate and run Core service 
    Core().run()

    # Instantiate the new scenario name hello_scenario from the scenario configuration built before
    hello_scenario = tp.create_scenario(scenario_cfg)

    # Run GUI
    Gui(page).run()