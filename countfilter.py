numbers = [10, 7, 4, 9, 12, 15, 8]

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even Numbers:", even)
print("Odd Numbers:", odd)
print("Count of Even:", len(even))
print("Count of Odd:", len(odd))