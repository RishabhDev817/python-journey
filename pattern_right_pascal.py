# Program to print a Right Pascal's Triangle (Half Diamond) star pattern

n = int(input("Enter number of rows for widest point: "))

print(f"\n--- Right Pascal's Triangle ({2 * n - 1} rows total) ---")

# Upper half (increasing)
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Lower half (decreasing)
for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

