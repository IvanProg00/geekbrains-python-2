from random import randint

period = int(input("Enter the period: "))

while period < 1 or period > 100:
    period = int(input("Period must be from 1 to 100: "))
count = 0
max_count = 0

for i in range(period):
    # temperature = int(input("Enter the temperature: "))
    temperature = randint(-50, 50)
    print(f"Temperature: {temperature}")

    if temperature <= 0:
        count = 0
    else:
        count += 1
        if count > max_count:
            max_count = count

print(f"The maximum days of thaw is {max_count}")
