class NegativeAgeError(Exception):
    pass


try:
    age = int(input("Enter age: "))

    if age < 0:
        raise NegativeAgeError("Age cannot be negative")

    year = 2026 - age
    print("Year of Birth =", year)

except NegativeAgeError as e:
    print("Error:", e)

except ValueError:
    print("Error: Enter numbers only")