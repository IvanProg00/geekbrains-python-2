import functions


while True:
    print('1. output, 2. add, 3. search, 4. update, 5. delete')
    mode = int(input())
    if mode == 1:
        functions.show_data()
    elif mode == 2:
        functions.add_data()
    elif mode == 3:
        functions.find_data()
    elif mode == 4:
        functions.update_data()
    elif mode == 5:
        functions.delete_data()
    else:
        break
