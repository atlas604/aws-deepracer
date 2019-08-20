def reward_function(params):
    
    all_wheels_on_track = params['all_wheels_on_track']
    progress = params['progress']
    steps = params['steps']
    speed = params['speed']
    
    if all_wheels_on_track and steps > 0:
        reward = progress / steps * (speed / 9)
    
    else:
        reward = 1e-3
    
    return float(reward)
