# Program to print a Butterfly star pattern

n = int(input("Enter size factor for butterfly wings: "))

print(f"\n--- Butterfly Pattern ({2 * n - 1} rows total) ---")

# Upper half of wings (rows 1 to n)
for i in range(1, n + 1):
    # Left stars
    for j in range(i):
        print("*", end="")
    # Middle spaces
    for j in range(2 * (n - i)):
        print(" ", end="")
    # Right stars
    for j in range(i):
        print("*", end="")
    print()

# Lower half of wings (rows n-1 down to 1)
for i in range(n - 1, 0, -1):
    # Left stars
    for j in range(i):
        print("*", end="")
    # Middle spaces
    for j in range(2 * (n - i)):
        print(" ", end="")
    # Right stars
    for j in range(i):
        print("*", end="")
    print()

