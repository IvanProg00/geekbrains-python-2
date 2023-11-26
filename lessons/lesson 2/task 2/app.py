from random import randint

# number = int(input("Enter the number: "))
number = randint(1, 30)

factorial = 1
count = 1


while count <= number:
    factorial *= count
    count += 1

print(f"Factorial of the {number} is {factorial}")
