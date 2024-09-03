# Function to compute the sum of two numbers
def sum_two_numbers(num1, num2):
    return num1 + num2
print(sum_two_numbers(16, 29))

# Function to determine if a number is Even/is divisible by 2
def check_even(num):
    return num % 2 == 0
print(check_even(8))
print(check_even(11))

# Function to reverse the given string first leter becomes the last one
def reverse_string(s):
    return s[::-1]
print(reverse_string("hello"))

# Function to calculate the number of vowels in a string ie.my name
def vowel_count(s):
    vowels = "aeiou"
    return sum(char in vowels for char in s.lower())
print(vowel_count("Jimmy Musyoki Mulundi"))

# method two
def vowel_count(s):
    vowels = "aeiou"
    return sum(char in vowels for char in s)
print(vowel_count("Jimmy Musyoki Mulundi"))  

# Function to compute the factorial of a given number
def factorial_of(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial_of(5))



# Decorator function that applies a simple decoration to another function
def simple_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@simple_decorator
def say_hello(name):
    print(f"Hello, {name}!")
say_hello("Jimmy")




