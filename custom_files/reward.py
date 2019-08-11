def reward_function(params):
    
    all_wheels_on_track = params['all_wheels_on_track']
    progress = params['progress']
    speed = params['speed']
    
    if all_wheels_on_track:
        reward = progress / 100 * speed
    
    else:
        reward = 1e-3
    
    return float(reward)
