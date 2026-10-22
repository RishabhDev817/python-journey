# Program to find unique words from a string using sets

text = input("Enter a sentence: ")

# 1. Convert to lowercase so "Hello" and "hello" are treated as the same word
# 2. Split string by spaces into a list of words
words_list = text.lower().split()

# 3. Strip common punctuation marks from each word
cleaned_words = [word.strip(".,!?;:\"'()[]{}") for word in words_list if word.strip(".,!?;:\"'()[]{}")]

# 4. Convert the list of words into a set to keep only unique words
unique_words = set(cleaned_words)

# Display the results
print("\nOriginal text:", text)
print("Total words:", len(cleaned_words))
print("Total unique words count:", len(unique_words))
print("Unique words set:", unique_words)
