print("Hello, Robotics World!")

robot_name = 'Chitti'
task_status = 'Idle'
print("Robot Name: " + robot_name, ", Task Status: " + task_status)

battery_level = 85
print(f"Battery Level: {battery_level}%")

with open('robot_log.txt', 'w') as log_file:
    log_file.write("Robot initialized successfully.\n")
    log_file.write(f"Robot Name: {robot_name}\n")
    log_file.write(f"Task Status: {task_status}\n")
    log_file.write(f"Battery Level: {battery_level}%\n")
