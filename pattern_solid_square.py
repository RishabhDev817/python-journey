# Program to print a Solid Square star pattern

n = int(input("Enter side length of the square: "))

print(f"\n--- Solid Square Star Pattern ({n}x{n}) ---")
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

