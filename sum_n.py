n = int(input("Enter a number : "))

total_sum = 0
i = 1

while i <= n:
    total_sum += i
    i += 1  

print("The sum of first", n, "natural numbers is:", total_sum)