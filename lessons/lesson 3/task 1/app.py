list_of_dicts = [
    {"V": "S001"},
    {"V": "S002"},
    {"VI": "S001"},
    {"VI": "S005"},
    {"VII": "S005"},
    {"V": "S009"},
    {"VIII": "S007"},
]
unique_values = set()

for i in list_of_dicts:
    for val in i.values():
        unique_values.add(val)

print(unique_values)
