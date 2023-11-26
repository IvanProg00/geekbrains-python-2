def show_data() -> None:
    """Outputs information from the directory"""
    with open("book.txt", "r", encoding="utf-8") as book:
        print(book.read())


def add_data() -> None:
    """Adds information to the directory"""
    fio = input("Enter fio: ")
    phone = input("Enter phone: ")
    with open("book.txt", "a", encoding="utf-8") as book:
        book.write(f"\n{fio} | {phone}")


def find_data() -> None:
    """Prints the search result in the directory"""
    with open("book.txt", "r", encoding="utf-8") as book:
        data = book.read()
    contact_to_find = input()
    result = search(data, contact_to_find)
    print(result)


def update_data() -> None:
    """Updates data from the file"""
    with open("book.txt", "r", encoding="utf-8") as book:
        data = book.readlines()

    line = input("Enter the line: ")
    index_line = find(data, line)
    if index_line == -1:
        print("Line not found")
        return

    print(f"Your line is \"{data[index_line].rstrip()}\"")
    fio = input("Enter new fio: ")
    phone = input("Enter new phone: ")
    data[index_line] = f"{fio} | {phone}\n"

    with open("book.txt", "w", encoding="utf-8") as book:
        book.writelines(data)


def delete_data() -> None:
    """Deletes data from the file"""
    with open("book.txt", "r", encoding="utf-8") as book:
        data = book.readlines()

    line = input("Enter the line: ")
    index_line = find(data, line)
    if index_line == -1:
        print("Line not found")
        return

    data.pop(index_line)

    with open("book.txt", "w", encoding="utf-8") as book:
        book.writelines(data, )


def search(book: str, info: str) -> list[str]:
    """Finds entries in the list by a specific search criterion"""
    lines = book.splitlines()
    info = info.lower()
    # return [contact for contact in lines if info in contact.lower()]
    return list(filter(lambda s: info in s.lower(), lines))


def find(book: list[str], info: str) -> int:
    info = info.lower()
    for i in range(len(book)):
        if info in book[i].lower():
            return i
    return -1
