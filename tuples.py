marks = (12,20,59,39,89)
         
print("studentsmarks: ", marks)

# lenth of tuple

print("Total Subjects: " ,[len(marks)])

# Acces elements using indexing
print("First Element: ", marks[0])
print("Last Element: ", marks[-1])

#Slicing tuple
print("Marks of middle students: ", marks[1:4])

#Check spicific marks exits or not
check_mark = int(input("Enter Marks to observe them"))
if check_mark in marks:
    print(check_mark,"is present in the marks")
else:
    print(check_mark, "is not present in the marks")

#Looop through the tuple
print("All Marks: ")
for m in marks:
    print(m)


#Joining two tples toughether
extra_marks = (95,90)
all_marks = marks+extra_marks
print("All marks after joining: " ,all_marks)

#Repeating
print("Repeted Marks: ", extra_marks * 2)
#step 9: Single element tuple
single_mark = (100,)
print("Single element tuple: ",single_mark)