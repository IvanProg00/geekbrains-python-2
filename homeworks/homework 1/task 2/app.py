"""
S
x + x = Petya, Sergio
2x = petya, sergio

2 * 2x = Katya
4x = Katya

2x + 4x = S
6x = S

x = S / 6
"""

total = int(input("Enter total number of cranes: "))

sergio = petya = total // 6
katya = sergio * 4


if sergio + petya + katya == total:
    print(f"Katya={katya} Sergio={sergio} Petya={petya}")
else:
    print("it is impossible to calculate")
