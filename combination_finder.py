
def custom_linear_counter(max_num_units, num_units, count_stopper):
    """
    Custom linear counter with a variable number of units.

    Parameters:
    - max_num_units (list): A list containing the maximum values for each unit.
    - num_units (list): A list containing the current values for each unit.
    - count_stopper (bool): A flag indicating whether the counting should stop.

    Returns:
    - num_units (list): Updated list of unit values.
    - count_stopper (bool): Updated flag indicating whether the counting should stop.
    
    Example use
    max_num_units = [2]
    num_runs = 100000000000000000000000000000
    run_count = 0
    num_units = [0]
    while run_count < num_runs:
        run_count += 1  # Increment the run count
        num_units, count_stopper = custom_linear_counter(max_num_units, num_units, count_stopper=False)
        if count_stopper:
            print(f"Stopping the loop max combinations reached! : {run_count}")
            break   
        print(num_units)
        if run_count == num_runs:
            print(f"Max runs reached! : {num_runs}") 
            break
    """
    
    if num_units is not None and max_num_units is not None: # Check if both num_units and max_num_units are provided
        
        if len(num_units) == 1: # Handle cases based on the length of num_units
            if num_units[0] < max_num_units[0]: # Check if the unit index 0 is less than the max number of units index 0
                num_units[0] += 1 # Increment the unit index 0 by 1
            elif num_units[0] == max_num_units[0]: # If it reaches the maximum, reset to 0 and add a new unit
                  num_units[0] = 0
                  num_units.append(1)
                 
        if len(num_units) == 2: # Handle cases based on the length of num_units
            if num_units[0] < max_num_units[0]: # Check if the unit index 0 is less than the max number of units index 0
                num_units[0] += 1 # Increment the unit index 0 by 1
            elif num_units[1] < max_num_units[0]: # Check if the unit index 1 is less than the max number of units index 0
                  num_units[0] = 1 # Reset units index 0 to 1
                  num_units[1] += 1 # Increment the unit index 1 by 1
            elif num_units[0] and num_units[1] == max_num_units[0]: # Check if the unit index 0 and unit index 1 is less than the max number of units index 0
                  num_units[0] = 0 # Reset units index 0 to 0
                  num_units[1] = 1 # Reset units index 1 to 1
                  num_units.append(1) # Add a new units value index
                  
        if len(num_units) == 3:# Handle cases based on the length of num_units
            if num_units[0] < max_num_units[0]: # Check if the unit index 0 is less than the max number of units index 0
                num_units[0] += 1 # Increment the unit index 0 by 1
            elif num_units[1] < max_num_units[0]: # Check if the unit index 1 is less than the max number of units index 0
                  num_units[0] = 1 # Reset units index 0 to 1
                  num_units[1] += 1 # Increment the unit index 1 by 1
            elif num_units[2] < max_num_units[0]: # Check if the unit index 2 is less than the max number of units index 0
                  num_units[0] = 1 # Reset units index 0 to 1
                  num_units[1] = 1 # Reset units index 1 to 1
                  num_units[2] += 1 # Increment the unit index 2 by 1
            elif num_units[0] and num_units[1] and num_units[2] == max_num_units[0]: # Check if the unit index 0 and unit index 1 and unit index 2 is less than the max number of units index 0
                  num_units[0] = 0 # Reset units index 0 to 1
                  num_units[1] = 1 # Reset units index 1 to 1
                  num_units[2] = 1 # Reset units index 2 to 1
                  num_units.append(1) # Add a new units value index

        if len(num_units) == 4:
            if num_units[0] < max_num_units[0]:
                num_units[0] += 1
            elif num_units[1] < max_num_units[0]:
                  num_units[0] = 1
                  num_units[1] += 1
            elif num_units[2] < max_num_units[0]:
                  num_units[0] = 1
                  num_units[1] = 1
                  num_units[2] += 1
            elif num_units[3] < max_num_units[0]:
                  num_units[0] = 1
                  num_units[1] = 1
                  num_units[2] = 1
                  num_units[3] += 1
            elif num_units[0] and num_units[1] and num_units[2] and num_units[3] == max_num_units[0]:
                  num_units[0] = 0
                  num_units[1] = 1
                  num_units[2] = 1
                  num_units[3] = 1
                  num_units.append(1)
                  
        if len(num_units) == 5:
            if num_units[0] < max_num_units[0]:
                num_units[0] += 1
            elif num_units[1] < max_num_units[0]:
                  num_units[0] = 1
                  num_units[1] += 1
            elif num_units[2] < max_num_units[0]:
                  num_units[0] = 1
                  num_units[1] = 1
                  num_units[2] += 1
            elif num_units[3] < max_num_units[0]:
                  num_units[0] = 1
                  num_units[1] = 1
                  num_units[2] = 1
                  num_units[3] += 1
            elif num_units[4] < max_num_units[0]:
                  num_units[0] = 1
                  num_units[1] = 1
                  num_units[2] = 1
                  num_units[3] = 1
                  num_units[4] += 1
            elif num_units[0] and num_units[1] and num_units[2] and num_units[3] and num_units[4] == max_num_units[0]:
                  num_units[0] = 0
                  num_units[1] = 1
                  num_units[2] = 1
                  num_units[3] = 1
                  num_units[4] = 1
                  num_units.append(1)
                 
        if len(num_units) == 6:
            if num_units[0] < max_num_units[0]:
                num_units[0] += 1
            elif num_units[1] < max_num_units[0]:
                  num_units[0] = 1
                  num_units[1] += 1
            elif num_units[2] < max_num_units[0]:
                  num_units[0] = 1
                  num_units[1] = 1
                  num_units[2] += 1
            elif num_units[3] < max_num_units[0]:
                  num_units[0] = 1
                  num_units[1] = 1
                  num_units[2] = 1
                  num_units[3] += 1
            elif num_units[4] < max_num_units[0]:
                  num_units[0] = 1
                  num_units[1] = 1
                  num_units[2] = 1
                  num_units[3] = 1
                  num_units[4] += 1
            elif num_units[5] < max_num_units[0]:
                  num_units[0] = 1
                  num_units[1] = 1
                  num_units[2] = 1
                  num_units[3] = 1
                  num_units[4] = 1
                  num_units[5] += 1
            elif num_units[0] and num_units[1] and num_units[2] and num_units[3] and num_units[4] and num_units[5] == max_num_units[0]:
                  num_units[0] = 0
                  num_units[1] = 1
                  num_units[2] = 1
                  num_units[3] = 1
                  num_units[4] = 1
                  num_units[5] = 1
                  num_units.append(1)
                  
        if len(num_units) == 7:
            if num_units[0] < max_num_units[0]:
                num_units[0] += 1
            elif num_units[1] < max_num_units[0]:
                  num_units[0] = 1
                  num_units[1] += 1
            elif num_units[2] < max_num_units[0]:
                  num_units[0] = 1
                  num_units[1] = 1
                  num_units[2] += 1
            elif num_units[3] < max_num_units[0]:
                  num_units[0] = 1
                  num_units[1] = 1
                  num_units[2] = 1
                  num_units[3] += 1
            elif num_units[4] < max_num_units[0]:
                  num_units[0] = 1
                  num_units[1] = 1
                  num_units[2] = 1
                  num_units[3] = 1
                  num_units[4] += 1
            elif num_units[5] < max_num_units[0]:
                  num_units[0] = 1
                  num_units[1] = 1
                  num_units[2] = 1
                  num_units[3] = 1
                  num_units[4] = 1
                  num_units[5] += 1
            elif num_units[6] < max_num_units[0]:
                  num_units[0] = 1
                  num_units[1] = 1
                  num_units[2] = 1
                  num_units[3] = 1
                  num_units[4] = 1
                  num_units[5] = 1
                  num_units[6] += 1
            elif num_units[0] and num_units[1] and num_units[2] and num_units[3] and num_units[4] and num_units[5] and num_units[6] == max_num_units[0]:
                count_stopper = True
                return num_units, count_stopper
    else:
       num_units = [0]
    return num_units, count_stopper


"""
Testing the def here this is the code use to run the def above
"""



max_num_units = [2]
num_runs = 100000000000000000000000000000
run_count = 0
num_units = [0]
while run_count < num_runs:
    run_count += 1  # Increment the run count
    num_units, count_stopper = custom_linear_counter(max_num_units, num_units, count_stopper=False)
    if count_stopper:
        print(f"Stopping the loop max combinations reached! : {run_count}")
        break   
    print(num_units)
    if run_count == num_runs:
        print(f"Max runs reached! : {num_runs}") 
        break
 
