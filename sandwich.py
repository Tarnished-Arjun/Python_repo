menu = {
    "Chicken": 120,
    "Beef": 150,
    "Veg": 100
}

order = input("Enter sandwich type: ").title()

if order in menu:
    print("Price =", menu[order])
else:
    print("Item not available")