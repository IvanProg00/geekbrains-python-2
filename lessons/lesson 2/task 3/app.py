from random import randint

num_melons = int(input("Enter the number of watermelons: "))

min_weight = 0
max_weight = 0

for i in range(num_melons):
    melon_weight = randint(1, 30_001)
    print(f"Melon weight: {melon_weight}")

    if melon_weight > max_weight or i == 0:
        max_weight = melon_weight

    if melon_weight < min_weight or i == 0:
        min_weight = melon_weight

print(
    f"Minimum weight of melons is {min_weight} and maximum weight of melons is {max_weight}")
