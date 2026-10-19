from analyzer import analyze_text

message = "I  love    Python."

cleaned_message = analyze_text(message)

print("Original message:", message)
print("Cleaned message:", cleaned_message)