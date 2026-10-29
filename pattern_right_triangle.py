# Program to print a Right-Angled Triangle star pattern

n = int(input("Enter number of rows: "))

print(f"\n--- Right-Angled Triangle ({n} rows) ---")
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

