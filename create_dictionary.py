# Creating a Dictionary of Robotics Components
robotics_components = {
    'Sensors': ['LIDAR', 'Camera', 'Ultrasonic', 'Infrared', 'GPS'],
    'Actuators': ['Motors', 'Servos', 'Hydraulics'],
    'Controllers': ['Microcontroller', 'PLC', 'Embedded System'],
    'Power Supply': ['Battery', 'Solar Panel', 'Fuel Cell']
}

# Print the dictionary
print("Robotics Components Dictionary:", robotics_components)

# Dictionary with various data types as values
robot_specs = {
    'Name': 'Chitti',
    'Speed': 2.5,  # in Tera Hertz
    'IsActive': True,
    'Dimensions': (1.8, 0.6, 0.5),
    'Sensors': {'LIDAR', 'Camera', 'Infrared'}
}
print("Robot Specifications:", robot_specs)

# Accessing elements in the dictionary
robot_name = robot_specs['Name']
print("Robot Name:", robot_name)

# modifying an element
robot_specs['Speed'] = 3.0
print("Updated Robot Speed:", robot_specs['Speed'])

# Adding a new component
robotics_components['Communication'] = ['WiFi', 'Bluetooth', 'Zigbee']
print("Updated Robotics Components Dictionary:", robotics_components)

# Merging two dictionaries
additional_components = {
    'Software': ['ROS', 'OpenCV', 'TensorFlow'],
    'Chassis': ['Wheeled', 'Tracked', 'Legged']
}

robotics_components.update(additional_components)
print("Merged Robotics Components Dictionary:", robotics_components)

software_used = robotics_components['Software']
print("Software Used in Robotics:", software_used)
