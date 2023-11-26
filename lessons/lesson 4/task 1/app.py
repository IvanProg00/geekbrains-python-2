# string = input("Enter the string: ")
string = "a a a b c a a d c d d"

letters = {}
res = ""

for letter in string.split(" "):
    num = letters.get(letter)
    if num is None:
        letters[letter] = 1
        res += letter + " "
    else:
        res += f"{letter}_{num} "
        letters[letter] += 1


print(res)
