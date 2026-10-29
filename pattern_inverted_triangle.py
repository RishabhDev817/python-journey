# Program to print an Inverted Right-Angled Triangle star pattern

n = int(input("Enter number of rows: "))

print(f"\n--- Inverted Right-Angled Triangle ({n} rows) ---")
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
