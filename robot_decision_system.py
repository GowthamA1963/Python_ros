# Robot movement decision system
obstacle_type = 'wall'

if obstacle_type == 'wall':
    print("Wall detected! Turn around.")
elif obstacle_type == 'small object':
    print("Small object detected! Slow down.")
elif obstacle_type == 'gap':
    print("Gap detected! Jump over it.")
else:
    print("No obstacles detected. Move forward.")

# Power aware decisions
battery_percentage = 15
if obstacle_type == 'wall' and battery_percentage > 20:
    print("Wall detected but sufficient battery. Attempting to climb over.")
elif obstacle_type == 'wall' and battery_percentage <= 20:
    print("Wall detected and low battery. Stopping to conserve power.")
elif obstacle_type == 'small object' and battery_percentage > 10:
    print("Small object detected and sufficient battery. Navigating around it.")
elif obstacle_type == 'small object' and battery_percentage <= 10:
    print("Small object detected and low battery. Stopping to conserve power.")
elif obstacle_type == 'gap' and battery_percentage > 30:
    print("Gap detected and sufficient battery. Jumping over it.")
elif obstacle_type == 'gap' and battery_percentage <= 30:
    print("Gap detected and low battery. Stopping to conserve power.")
else:
    print("No obstacles detected. Move forward.")
