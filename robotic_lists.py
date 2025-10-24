sensor_readings = [20, 55, 75, 0, 100]
print("Initital Sensor Readings: ", sensor_readings)

# Accessing elements
print("First Sensor Reading: ", sensor_readings[0])
print("Most Recent Sensor Reading: ", sensor_readings[-1])

# Updating a Sensor Reading
sensor_readings[2] = 80
print("Updated Sensor Readings: ", sensor_readings)

# New Sensor Readings List
sensor_readings.append(90)
print("New Sensor Readings: ", sensor_readings)

# Extending the list with multiple readings
sensor_readings.extend([65, 82, 73, 95, 88])
print("Extended Sensor Readings: ", sensor_readings)

# Removing a faulty reading
sensor_readings.remove(20)
print("Sensor Readings after removal: ", sensor_readings)

# Iterating through the list
print("Iterating through Sensor Readings:")
for reading in sensor_readings:
    print(reading)
