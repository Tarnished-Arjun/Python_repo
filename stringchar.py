text = input("Enter a string: ")

first = text[0]
middle = text[len(text) // 2]
last = text[-1]

result = first + middle + last

print("New string:", result)