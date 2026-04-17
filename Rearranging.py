text = input("Enter a string: ")

lowercase = ""
uppercase = ""

for ch in text:
    if ch.islower():
        lowercase += ch
    else:
        uppercase += ch

result = lowercase + uppercase

print("Rearranged string:", result)