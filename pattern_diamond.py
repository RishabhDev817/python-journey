# Program to print a Diamond star pattern

n = int(input("Enter number of rows for upper half: "))

print(f"\n--- Diamond Star Pattern ({2 * n - 1} rows total) ---")

# Upper half (including middle row)
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

# Lower half
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

