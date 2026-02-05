# String programs

text = "Python Basics"

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
if "Python" in text:
    print("Substring found")
