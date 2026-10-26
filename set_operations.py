# Program demonstrating fundamental set operations in Python

# Sample sets of programming languages
set_a = {"Python", "Java", "C++", "JavaScript"}
set_b = {"Python", "Go", "Rust", "Java"}

print("Set A:", set_a)
print("Set B:", set_b)

# 1. Union: Elements present in either set A or set B or both
union_set = set_a | set_b
print("\nUnion (A | B):", union_set)

# 2. Intersection: Elements present in both set A and set B
intersection_set = set_a & set_b
print("Intersection (A & B):", intersection_set)

# 3. Difference: Elements in set A but not in set B
difference_a_b = set_a - set_b
print("Difference (A - B):", difference_a_b)

# 4. Difference: Elements in set B but not in set A
difference_b_a = set_b - set_a
print("Difference (B - A):", difference_b_a)

# 5. Symmetric Difference: Elements in A or B, but not both
sym_diff = set_a ^ set_b
print("Symmetric Difference (A ^ B):", sym_diff)
