def same_by1(characteristic, objects):
    for o in objects:
        if not characteristic(o):
            return False
    return True


def same_by2(characteristic, objects):
    new = list(filter(characteristic, objects))

    return len(new) == len(objects)


values = [1, 2, 3, 4, 5]

result1 = same_by1(lambda x: x % 2 == 0, values)
print(result1)


result2 = same_by2(lambda x: x % 2 == 0, values)
print(result2)
