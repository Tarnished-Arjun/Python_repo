nums = (1, 2, 3, 4, 5, 6, 7, 8)

even = ()

for n in nums:
    if n % 2 == 0:
        even = even + (n,)

print("Original Tuple:", nums)
print("Even Tuple:", even)