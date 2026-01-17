shopping_list = ["apple", "rice", "eggs", "butter", "cheese"]

print(shopping_list)
print(len(shopping_list))

print(shopping_list[0])
print(shopping_list[-1])

print(shopping_list[0:-1])

shopping_list.append("chocolate")
shopping_list.insert(1, "milk")

del shopping_list[2]

print("apple" in shopping_list)
print("bread" not in shopping_list)

for item in shopping_list:
    print(item)

item_lengths = [len(item) for item in shopping_list]

print(shopping_list)
print(item_lengths)
