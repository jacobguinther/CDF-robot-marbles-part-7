from cadCAD.configuration.utils import config_sim
from cadCAD.configuration import Experiment
from models.state_variables import genesis_states
from models.psubs import partial_state_update_blocks

simulation_parameters = {
        'T': range(10),
        'N': 50, # We'll run the same simulation 50 times; the random events in each simulation are independent
        'M': {
            'capacity' : [
                { 'robot_1': 1, 'robot_2': 1 }, # Each robot has capacity 1
                { 'robot_1': 2, 'robot_2': 1 }, # Arm 1 has been "upgraded"
                { 'robot_1': 2, 'robot_2': 2 }  # Both arms have been "upgraded"
            ]
        }
    }


exp = Experiment()    # this is the creation of the experiment object that must appear in the Labs.py
c = config_sim(simulation_parameters)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# The configurations above are then packaged into a `Configuration` object
# #.append_model    <-- append model is the new way to do this in the future, append config is the old way.
exp.append_configs(   
    model_id = 'sys_model',
    initial_state=genesis_states, #dict containing variable names and initial values
    partial_state_update_blocks=partial_state_update_blocks, #dict containing state update functions
    sim_configs=c #preprocessed dictionaries containing simulation parameters
)