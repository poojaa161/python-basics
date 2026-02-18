

text = "you create reality"

print("Original Text:", text)

# Length of string
print("Length:", len(text))

# Convert to uppercase
print("Uppercase:", text.upper())

# Convert to lowercase
print("Lowercase:", text.lower())

# Reverse string
reversed_text = text[::-1]
print("Reversed:", reversed_text)

# Check substring
if "create" in text:
    print("Substring 'create' found")

# Replace word
new_text = text.replace("reality", "your future")
print("After Replace:", new_text)

# Count vowels
vowels = "aeiou"
count = 0
for char in text:
    if char in vowels:
        count += 1
print("Number of vowels:", count)

# Split string
words = text.split()
print("Split words:", words)


# check palindrome
check_word = "level"
if check_word == check_word[::-1]:
    print(check_word, "is a palindrome")
else:
    print(check_word, "is not a palindrome")
