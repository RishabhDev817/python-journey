# Program to find unique vowels and their frequencies in a string using sets

text = input("Enter a sentence: ")

# Define vowel set
vowels = {"a", "e", "i", "o", "u"}

# Clean text to lowercase
normalized_text = text.lower()

# Find unique vowels present using set intersection
found_vowels = set(normalized_text) & vowels

# Count total vowels and individual frequencies
total_vowel_count = sum(normalized_text.count(v) for v in found_vowels)

print("\n--- Vowel Analysis ---")
print("Unique vowels present:", sorted(found_vowels))
print("Total number of unique vowels:", len(found_vowels))
print("Total vowel occurrences:", total_vowel_count)

print("\nFrequency breakdown:")
for vowel in sorted(found_vowels):
    print(f"  '{vowel}': {normalized_text.count(vowel)} time(s)")
