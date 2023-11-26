ticket = int(input("Enter the ticket: "))

right_sum = 0

for _ in range(3):
    right_sum += ticket % 10
    ticket //= 10

left_sum = 0

for _ in range(3):
    left_sum += ticket % 10
    ticket //= 10

if right_sum == left_sum:
    print("yes")
else:
    print("no")
