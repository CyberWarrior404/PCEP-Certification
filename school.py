students = ["STUDENT DATABASE:",("Jessi",1234,11),("Bob",4321,10),("Harry",1919,12)]
print(students)
while True:
     name = input("Enter name: ")
     student_id = input("Enter student ID: ")
     age = input("Enter age: ")

     student_info = (name,student_id,age)

     students.append(student_info)
     break

print(students)
