# Function to compute the sum of two numbers
def add_numbers(num1, num2):
    return num1 + num2
print(add_numbers(16, 29))







# Function to determine if a number is Even/is divisible by 2
def is_even(num):
    return num % 2 == 0
print(is_even(8))
print(is_even(11))










# Function to reverse the given string first leter becomes the last one
def reverse_string(s):
    return s[::-1]
print(reverse_string("hello"))










# Function to calculate the number of vowels in a string ie.my name
def count_vowels(s):
    vowels = "aeiou"
    return sum(char in vowels for char in s.lower())
print(count_vowels("Jimmy Musyoki Mulundi"))

# method two
def count_vowels(s):
    vowels = "aeiou"
    return sum(char in vowels for char in s)
print(count_vowels("Jimmy Musyoki Mulundi"))  











# Function to compute the factorial of a given number
def calculate_factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(calculate_factorial(5))












# Decorator function
def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

# Function to apply the decorator
def apply_decorator(func):
    decorated_func = decorator_func(func)
    return decorated_func

# Example function to be decorated
def say_hello(name):
    print(f"Hello, {name}!")

# Applying the decorator using the apply_decorator function
decorated_say_hello = apply_decorator(say_hello)

# Call the decorated function
decorated_say_hello("Jimmy")













# Function to order a list of tuples based on age
def sort_by_age(people_list):
    return sorted(people_list, key=lambda person: person[1])
people = [("jimmy", 74), ("mulundi", 55), ("musyoki", 27),("kalama", 24), ("erick", 35), ("degrace", 18)]
print(sort_by_age(people))





# Function to combine two dictionaries with value addition for common keys
def merge_dicts(dict_a, dict_b):
    combined = dict_a.copy()
    for key, value in dict_b.items():
        if key in combined:
            combined[key] += value
        else:
            combined[key] = value
    return combined
dict_a = {'a': 9, 'b': 5}
dict_b = {'b': 3, 'c': 7}
print(merge_dicts(dict_a, dict_b))








# Class to represent a car with attributes and a method to display information
class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def show_details(self):
        print(f"Vehicle Make: {self.make}")
        print(f"Vehicle Model: {self.model}")
        print(f"Vehicle Year: {self.year}")

my_vehicle = car("G-wagon", "Camry", 2024)
my_vehicle.show_details()