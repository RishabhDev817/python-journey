from app.analyzer import count_words
from app.cleaner import normalize_text

text = "I   love   Python programming."

cleaned = normalize_text(text)
words = count_words(cleaned)

print("Original text: ", text)
print("Cleaned text: ", cleaned)
print("Number of words: ", words)

