import taipy as tp

from taipy import Config
from taipy import Core

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

if __name__ == "__main__":
    # Instantiate and run Core service 
    Core().run()

    # Instantiate the new scenario name hello_scenario from the scenario configuration built before
    hello_scenario = tp.create_scenario(scenario_cfg)

    # sets the input data node input_name of hello_scenario with the string value 
    hello_scenario.input_name.write("In God We Trust !")

    # submits the hello_scenario for execution, which triggers the creation and execution of a job
    hello_scenario.submit()

    # reads and prints the output data node message written by the execution of the scenario hello_scenario
    print(hello_scenario.message.read())