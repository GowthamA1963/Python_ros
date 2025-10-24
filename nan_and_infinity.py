import math


# Positive infinity
positive_infinity = float('inf')
print(f"Positive Infinity: {positive_infinity}")

# Negative infinity
negative_infinity = float('-inf')
print(f"Negative Infinity: {negative_infinity}")


# Not a Number (NaN)
nan_value = float('nan')
print(f"NaN Value: {nan_value}")

addition = 2 + nan_value
print(f"2 + NaN = {addition}")


print('Is NaN:', math.isnan(nan_value))
