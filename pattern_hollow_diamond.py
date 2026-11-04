# Program to print a Hollow Diamond star pattern

n = int(input("Enter number of rows for upper half: "))

print(f"\n--- Hollow Diamond Star Pattern ({2 * n - 1} rows total) ---")

# Upper half (rows 1 to n)
for i in range(1, n + 1):
    # Leading spaces
    for j in range(n - i):
        print(" ", end="")
    # First star
    print("*", end="")
    # Inner spaces and second star
    if i > 1:
        for j in range(2 * i - 3):
            print(" ", end="")
        print("*", end="")
    print()

# Lower half (rows n-1 down to 1)
for i in range(n - 1, 0, -1):
    # Leading spaces
    for j in range(n - i):
        print(" ", end="")
    # First star
    print("*", end="")
    # Inner spaces and second star
    if i > 1:
        for j in range(2 * i - 3):
            print(" ", end="")
        print("*", end="")
    print()
