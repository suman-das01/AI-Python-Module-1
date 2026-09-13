# Day 4 - Functions and Beginner Programs


# Function to greet
def greet(name):
    return "Hello, " + name


print(greet("Suman"))


# Addition Function
def add(a, b):
    return a + b


print("Addition:", add(10, 20))


# Even or Odd
def check_even_odd(number):

    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print("10 is:", check_even_odd(10))
print("15 is:", check_even_odd(15))


# Square of a number
def square(number):
    return number * number


print("Square:", square(5))


# Factorial
def factorial(number):

    result = 1

    for i in range(1, number + 1):
        result = result * i

    return result


print("Factorial of 5:", factorial(5))


# Find largest of two numbers
def largest(a, b):

    if a > b:
        return a
    else:
        return b


print("Largest:", largest(25, 40))


# Simple Calculator
def calculator(a, b, operator):

    if operator == "+":
        return a + b

    elif operator == "-":
        return a - b

    elif operator == "*":
        return a * b

    elif operator == "/":

        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"

    else:
        return "Invalid operator"


print("Calculator:", calculator(20, 5, "+"))
print("Calculator:", calculator(20, 5, "*"))
