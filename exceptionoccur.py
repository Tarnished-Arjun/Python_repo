a = 12
s = "Hello"

try:
    print(a + s)
except TypeError:
    print("Error: Cannot add integer and string")