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

# Function to calculate the number of vowels in a string
def vowel_count(s):
    vowels = "aeiou"
    return sum(char in vowels for char in s)
print(vowel_count("Jimmy Musyoki Mulundi"))  # Example usage with vowels