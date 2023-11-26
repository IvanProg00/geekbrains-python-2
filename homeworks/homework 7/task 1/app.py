def count_vowels(s):
    count = 0
    for c in s:
        if c in ["а", "о", "и", "ы", "у", "э", "ю", "e", "ё"]:
            count += 1

    return count


def check_rithm(phrases):
    num_vowels = count_vowels(phrases[0])

    for i in range(1, len(phrases)):
        if count_vowels(phrases[i]) != num_vowels:
            return False

    return True


phrases = input("Enter the poem: ").split()
# phrases = "пара-ра-рам рам-пам-папам па-ра-па-да".split()

is_rithm = check_rithm(phrases)

if is_rithm:
    print("Парам пам-пам")
else:
    print("Пам парам")
