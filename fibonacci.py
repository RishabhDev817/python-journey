n = int(input("Enter the number of terms: "))

a, b = 0, 1

print(f"Fibonacci sequence ({n} terms):")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()
