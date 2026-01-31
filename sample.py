text = "I Love Coding"
print("original string: ", text)
print("length of string: ",len(text))
print("frist charecter: ", text[0])
print("last charecter: ", text[-1])
print("\nlooping through charecters: ")
for ch in text:
    print(ch,end=" ")
print()

print("\nusing in and not in operators: ")
print("'Love' in text: ", "Love" in text)
print("'JAVA' not in text: ", "JAVA" not in text)

