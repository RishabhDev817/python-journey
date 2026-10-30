# Program to print an Hourglass star pattern

n = int(input("Enter number of rows for top half: "))

print(f"\n--- Hourglass Star Pattern ({2 * n - 1} rows total) ---")

# Upper half (Inverted pyramid down to middle single star)
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

# Lower half (Upright pyramid expanding from 2 to n)
for i in range(2, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

