# Palindrome Checker

text = input("Enter word/number: ")

# Original value
print("Original:", text)

# Reverse the text
reversed_text = text[::-1]
print("Reversed:", reversed_text)

# Convert to lowercase for comparison (ignore case)
if text.lower() == reversed_text.lower():
    print("Result: PALINDROME")
else:
    print("Result: NOT A PALINDROME")