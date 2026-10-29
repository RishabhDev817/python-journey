# Program to print a Pyramid (Equilateral Triangle) star pattern

n = int(input("Enter number of rows: "))

print(f"\n--- Pyramid Star Pattern ({n} rows) ---")
for i in range(1, n + 1):
    # Print leading spaces
    for j in range(n - i):
        print(" ", end="")
    # Print stars
    for k in range(2 * i - 1):
        print("*", end="")
    print()

