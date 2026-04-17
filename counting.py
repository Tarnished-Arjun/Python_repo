text = input("Enter a string: ")

for ch in text:
    count = text.count(ch)
    print(ch, "=", count)