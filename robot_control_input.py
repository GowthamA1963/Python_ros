threshold = input("Enter sensor threshold value: ")
threshold = float(threshold)

print(f'Sensor threshold set to: {threshold}')

sensor_value = 85.0  # Example sensor value

if sensor_value > threshold:
    print("Alert: Sensor value exceeds the threshold!")
else:
    print("Sensor value is within acceptable limits.")
