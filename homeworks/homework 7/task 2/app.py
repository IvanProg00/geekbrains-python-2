def transform(info: str):
    return tuple(map(lambda s: tuple(s.split("=")), info.split(" ")))


data = input("Enter line: ")
print(transform(data))
