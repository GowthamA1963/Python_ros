# Creating a set of robotics-related terms
sensor_ids = {'LIDAR', 'Camera', 'Ultrasonic', 'Infrared', 'GPS'}
print("Unquue Sensor IDs: ", sensor_ids)

sensor_ids.update(['LIDAR', 'Camera', 'Thermal'])
print("Sensor IDs after adding duplicates: ", sensor_ids)
# Sets automatically handle duplicates, so 'LIDAR' and 'Camera' won't be added again

sensor_ids.add('Pressure')
sensor_ids.discard('GPS')
print("Sensor IDs after adding Pressure and removing GPS: ", sensor_ids)

another_set = {'Gyroscope', 'Accelerometer', 'Infrared'}
combined_sensors = sensor_ids.union(another_set)
print("Combined Sensor IDs: ", combined_sensors)

common_sensors = sensor_ids.intersection(another_set)
print("Common Sensor IDs: ", common_sensors)
