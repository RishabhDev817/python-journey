# Program to check if two strings are anagrams of each other

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Normalize: remove spaces and convert to lowercase
clean1 = str1.replace(" ", "").lower()
clean2 = str2.replace(" ", "").lower()

# Check using sorted characters
is_anagram = sorted(clean1) == sorted(clean2)

# Check unique character sets
set1 = set(clean1)
set2 = set(clean2)

print("\n--- Results ---")
print(f"Unique characters in '{str1}':", set1)
print(f"Unique characters in '{str2}':", set2)

if is_anagram:
    print(f"\n'{str1}' and '{str2}' are ANAGRAMS!")
else:
    print(f"\n'{str1}' and '{str2}' are NOT anagrams.")
