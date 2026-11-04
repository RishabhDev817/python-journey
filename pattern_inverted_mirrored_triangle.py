# Program to print an Inverted Mirrored (Right-Aligned) Triangle star pattern

n = int(input("Enter number of rows: "))

print(f"\n--- Inverted Mirrored Triangle ({n} rows) ---")
for i in range(n):
    # Print leading spaces
    for j in range(i):
        print(" ", end=" ")
    # Print stars
    for k in range(n - i):
        print("*", end=" ")
    print()

