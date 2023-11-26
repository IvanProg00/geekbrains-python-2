width = int(input("Enter chocolate width: "))
height = int(input("Enter chocolate height: "))
num_parts = int(input("Enter the number of parts: "))

if num_parts > width * height:
    print("Chocolate is not so big")
elif num_parts % width == 0 or num_parts % height == 0:
    print("yes")
else:
    print("no")
