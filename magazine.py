class Magazine:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Magazine.count += 1


m1 = Magazine("India Today", 50)
m2 = Magazine("Forbes", 100)
m3 = Magazine("Sportstar", 60)

print("Total Objects Created:", Magazine.count)