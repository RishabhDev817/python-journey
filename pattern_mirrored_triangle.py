# Program to print a Mirrored (Right-Aligned) Right-Angled Triangle star pattern

n = int(input("Enter number of rows: "))

print(f"\n--- Mirrored Right-Angled Triangle ({n} rows) ---")
for i in range(1, n + 1):
    # Print leading spaces
    for j in range(n - i):
        print(" ", end=" ")
    # Print stars
    for k in range(i):
        print("*", end=" ")
    print()

