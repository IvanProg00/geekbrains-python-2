# string = input("Enter the string: ")
string = "She sells sea shells on the sea shore The shells that she sells are sea \
shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells \
are sea shore shells"
string = "кот собака \nсобака\n кот\n"

words = string.lower().split(" ")
unique_words = set()

for word in words:
    unique_words.add(word.strip())

num_unique_words = len(unique_words)
print(num_unique_words)
