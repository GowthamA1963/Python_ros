# filters
def is_even(number):
    return number % 2 == 0


numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(is_even, numbers))
print('Even numbers:', even_numbers)
