def show_data() -> None:
    """Outputs information from the directory"""
    with open("book.txt", "r", encoding="utf-8") as book:
        print(book.read())


def add_data() -> None:
    """Adds information to the directory"""
    fio = input()
    phone = input("")
    with open("book.txt", "a", encoding="utf-8") as book:
        book.write(f"\n{fio} | {phone}")


def find_data() -> None:
    """Prints the search result in the directory"""
    with open("book.txt", "r", encoding="utf-8") as book:
        data = book.read()
    contact_to_find = input()
    result = search(data, contact_to_find)
    print(result)


def search(book: str, info: str) -> list[str]:
    """Finds entries in the list by a specific search criterion"""
    lines = book.splitlines()
    info = info.lower()
    # return [contact for contact in lines if info in contact.lower()]
    return list(filter(lambda s: info in s.lower(), lines))
