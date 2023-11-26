num = int(input('Enter the number of coins: '))

num_tail_up = 0
num_tail_down = 0

for i in range(num):
    coin = int(input("Enter 0 if the coin is tails up and 1 if it's tail down: "))

    if coin == 0:
        num_tail_up += 1
    else:
        num_tail_down += 1


num_coins_to_flip = num_tail_down

if num_tail_up < num_tail_down:
    num_coins_to_flip = num_tail_up

print(f'You need to flip {num_coins_to_flip} coins')
