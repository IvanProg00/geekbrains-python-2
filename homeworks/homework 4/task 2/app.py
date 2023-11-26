number_of_bushes = int(input("Enter the number of bushes: "))
bushes = []

for i in range(number_of_bushes):
    bushes.append(int(input("Enter the number of berries: ")))


cherry_count = list()

for i in range(number_of_bushes - 1):
    cherry_count.append(bushes[i - 1] + bushes[i] + bushes[i + 1])

cherry_count.append(bushes[-2] + bushes[-1] + bushes[0])
max_cherries = max(cherry_count)
print(f"Max number of berries per bush are {max_cherries}")
