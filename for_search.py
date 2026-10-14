nums_tuple = (1 , 4,  9, 16, 25, 36, 49, 64, 81, 100)

x = int(input("Enter a number to search for: "))

found = False

for index, element in enumerate(nums_tuple):
    if element == x:
        print(f"Number {x} found at index {index}.")
        found = True
        break

if not found:
    print(f"Number {x} is not present in the tuple.")