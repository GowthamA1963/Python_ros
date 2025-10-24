# if-else statement for robot movement

obstacle_detected = True

if obstacle_detected:
    print("Obstacle detected! Stopping the robot.")
else:
    print("Path is clear. Moving forward.")

# Using elif for sensor based conditions
sensor_value = 'low_battery'

if sensor_value == 'obstacle':
    print("Obstacle detected! Stopping the robot.")
elif sensor_value == 'low_battery':
    print("Low battery! Returning to charging station.")
else:
    print("All systems normal. Continuing operation.")

# Nested if statements for complex decision making
if sensor_value == 'obstacle':
    distance_to_obstacle = 15  # in cm
    if distance_to_obstacle < 10:
        print("Too close to obstacle! Stopping immediately.")
    else:
        print("Obstacle detected but at a safe distance. Slowing down.")
else:
    print("No obstacles detected. Proceeding as planned.")


# Logical Operatorrs in robot decisions
battery_level = 20  # percentage
if sensor_value == 'obstacle' and battery_level < 25:
    print("Obstacle detected and low battery! Stopping and returning to base.")
elif sensor_value == 'obstacle' or battery_level < 25:
    print("Either obstacle detected or low battery. Proceeding with caution.")
else:
    print("All systems normal. Continuing operation.")
