def reward_function(params):
    
    all_wheels_on_track = params['all_wheels_on_track']
    progress = params['progress']
    steps = params["steps"]
    
    if all_wheels_on_track and steps > 0:
        reward = (progress / steps) * 100
    
    else:
        reward = -1
    
    return float(reward)
