vitya_num = int(input("Enter vitia's number"))
train_num = int(input("Enter train's number"))

if vitya_num == train_num:
    print("It's impossible to calculate the size of the train")
else:
    res = vitya_num + train_num - 1
    print(res)
