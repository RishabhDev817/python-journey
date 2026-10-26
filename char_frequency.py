# Program to calculate frequency of each unique character in a string using sets

text = input("Enter a string: ")

# Extract unique characters using set, ignoring whitespace
unique_chars = sorted(set(text.replace(" ", "")))

print("\n--- Character Frequencies ---")
print(f"Unique characters ({len(unique_chars)}):", unique_chars)
print("\nCounts:")
for char in unique_chars:
    count = text.count(char)
    print(f"  '{char}' -> {count}")
