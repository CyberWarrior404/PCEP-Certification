fruits = ("strawberry","blackberry","blueberry")
print(fruits)
length = len(fruits)
print(length)
print(fruits[1])
for i in fruits:
    print(i)
fruit_list = list(fruits)

fruit_list.append("rasberry")
fruits=tuple(fruit_list)
print(fruits)

fruit_list= list(fruits)
fruit_list.insert(1,"gooseberry")
fruits=tuple(fruit_list)
print(fruits)