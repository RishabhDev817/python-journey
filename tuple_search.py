nums_tuple = (1 , 4,  9, 16, 25, 36, 49, 64, 81, 100)

x = int(input("Enter a number to search for : "))

index = 0
found = False

while index < len(nums_tuple):
    if nums_tuple[index] == x:
        found = True
        break
    index += 1

if not found:
    print(x, "is not present in the tuple.")
