text = "I Love Coding"

print("Original string:", text)
print("Length of string:", len(text))
print("First character:", text[0])
print("Last character:", text[-1])

print("\nLooping through characters:")
for ch in text:
    print(ch, end=" ")
print()

print("\nin and not in operators:")
print("'Love' in text:", "Love" in text)
print("'JAVA' not in text:", "JAVA" not in text)

print("\nstring methods:")
print("Lowercase:", text.lower())
print("Uppercase:", text.upper())
print("Capitalize:", text.capitalize())
print("Title case:", text.title())
print("Swapcase:", text.swapcase())


