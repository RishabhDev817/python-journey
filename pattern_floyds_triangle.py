# Program to print Floyd's Triangle number pattern

n = int(input("Enter number of rows: "))

print(f"\n--- Floyd's Triangle ({n} rows) ---")
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

