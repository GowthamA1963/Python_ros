import random

# Generate a random integer between 1 and 10
random_integer = random.randint(1, 10)
print(f"Random Integer: {random_integer}")

# Generate a random float between 0.0 and 1.0
random_float = random.random()
print(f"Random Float: {random_float}")

# Generate a float between 0.0 and 5.0
random_float_range = random.random() * 5
print(f"Random Float between 0.0 and 5.0: {random_float_range}")

# Choose a random element from a list
colors = ['Red', 'Blue', 'Green', 'Yellow', 'Black']
random_color = random.choice(colors)
print(f"Random Color: {random_color}")

# Shuffle a list of numbers
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"Shuffled Numbers: {numbers}")
