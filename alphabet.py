text = input("Enter a string: ")

words = text.split()

for word in words:
    if any(ch.isalpha() for ch in word) and any(ch.isdigit() for ch in word):
        print(word)