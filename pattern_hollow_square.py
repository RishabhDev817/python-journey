# Program to print a Hollow Square star pattern

n = int(input("Enter side length of the square: "))

print(f"\n--- Hollow Square Star Pattern ({n}x{n}) ---")
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

