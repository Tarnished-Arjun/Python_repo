# Sandwich.py

order = input("Enter sandwich type: ").lower()

match order:
    case "chicken":
        print("Price = 120")
    case "beef":
        print("Price = 150")
    case "veg":
        print("Price = 100")
    case _:
        print("Item not available")