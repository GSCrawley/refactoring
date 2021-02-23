# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)
Well_Done = 900000
Medium = 600000
Cooked_Constant = 0.05

def cooking_criteria(time, temperature, pressure, desired_state):
    if desired_state == 'well-done' and time * temperature * pressure * COOKED_CONSTANT >= WELL_DONE: 
        return True
    if desired_state == 'medium' and time * temperature * pressure * COOKED_CONSTANT >= MEDIUM:
        return True
    return False