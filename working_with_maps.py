def celcius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


temperatures_celcius = [0, 20, 37, 100]
temperatures_fahrenheit = list(map(celcius_to_fahrenheit, temperatures_celcius))
print('Temperatures in Fahrenheit:', temperatures_fahrenheit)
