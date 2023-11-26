values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def transformation(a):
    return a


transormed_values = list(map(transformation, values))
print(transormed_values)


transormed_values = list(map(lambda a: a, values))
print(transormed_values)
