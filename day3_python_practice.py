# Day 3 - Lists, Conditions and Loops


# List
numbers = [10, 20, 30, 40, 50]

print("Numbers:", numbers)
print("First number:", numbers[0])
print("Last number:", numbers[-1])


# Adding an element
numbers.append(60)

print("After adding 60:", numbers)


# For Loop
print("\nNumbers using for loop:")

for number in numbers:
    print(number)


# Even Numbers
print("\nEven Numbers:")

for number in numbers:
    if number % 2 == 0:
        print(number)


# Odd Numbers
print("\nOdd Numbers:")

for number in numbers:
    if number % 2 != 0:
        print(number)


# Sum of numbers
total = 0

for number in numbers:
    total = total + number

print("\nSum:", total)


# Find maximum number
print("Maximum:", max(numbers))

# Find minimum number
print("Minimum:", min(numbers))


# While Loop
print("\nWhile Loop:")

count = 1

while count <= 5:
    print(count)
    count += 1
