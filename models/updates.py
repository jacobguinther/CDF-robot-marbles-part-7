# We specify the robot arm's logic in a Policy Function
def robot_arm(params, step, sH, s):
    add_to_A = 0
    if (s['box_A'] > s['box_B']):
        add_to_A = -1
    elif (s['box_A'] < s['box_B']):
        add_to_A = 1
    return({'add_to_A': add_to_A, 'add_to_B': -add_to_A})


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# We make the state update functions less "intelligent",
# ie. they simply add the number of marbles specified in _input 
# (which, per the policy function definition, may be negative)
def increment_A(params, step, sH, s, _input):
    y = 'box_A'
    x = s['box_A'] + _input['add_to_A']
    return (y, x)

def increment_B(params, step, sH, s, _input):
    y = 'box_B'
    x = s['box_B'] + _input['add_to_B']
    return (y, x)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# We specify each of the robots logic in a Policy Function
robots_periods = [2,3] # Robot 1 acts once every 2 timesteps; Robot 2 acts once every 3 timesteps

def get_current_timestep(cur_substep, s):
    if cur_substep == 1:
        return s['timestep']+1
    return s['timestep']

def robot_arm_1(params, step, sH, s):
    _robotId = 1
    if get_current_timestep(step, s)%robots_periods[_robotId-1]==0: # on timesteps that are multiple of 2, Robot 1 acts
        return robot_arm(params, step, sH, s)
    else:
        return({'add_to_A': 0, 'add_to_B': 0}) # for all other timesteps, Robot 1 doesn't interfere with the system

def robot_arm_2(params, step, sH, s):
    _robotId = 2
    if get_current_timestep(step, s)%robots_periods[_robotId-1]==0: # on timesteps that are multiple of 3, Robot 2 acts
        return robot_arm(params, step, sH, s)
    else:
        return({'add_to_A': 0, 'add_to_B': 0}) # for all other timesteps, Robot 2 doesn't interfere with the system

