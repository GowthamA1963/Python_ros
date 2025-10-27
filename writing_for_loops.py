# Simple for loop with a list of colors

colors = ["red", "green", "blue", "yellow"]
for color in colors:
    print('Color:', color)

# For loop with range
for i in range(5):
    print('Number:', i)

# Interating over a string
for chr in "robotics":
    print('Character:', chr)


# Looping through a dictionary
robotics_components = {'wheels': 4, 'sensors': 5, 'motors': 2}
for component, quantity in robotics_components.items():
    print(f'Component: {component}, Quantity: {quantity}')

# Nested for loop
for outer in range(3):
    for inner in range(3):
        print(f'Outer: {outer}, Inner: {inner}')

# pattern printing using for loop
for i in range(1, 6):
    for j in range(i):
        print('*', end='')
    print()  # for new line
