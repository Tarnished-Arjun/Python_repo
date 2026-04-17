words = ["Python", "", "Code", "", "", "AI", ""]


new_list = []

for word in words:
    if word != "":
        new_list.append(word)

print("Original List:", words)
print("After Removing Empty Strings:", new_list)