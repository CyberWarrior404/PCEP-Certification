def lazy_function():
    pass

print("Lazu Function Output: ", lazy_function())

def hello():
    print("Hello! Welcom to PCEP Course")

hello()

def greet(name):
    print("Hello", name)

greet("Nameerah !")

# Functions with Return Values

def add(a,b):
    return a+b

result = add(5,3)
print("Addition Results: ", result)

#Functions with parameter value

def power_switch(state = True):
    return state

print("Power_Switch ", power_switch())
print("Power_Switch ", power_switch(False))

# Positional Argumemnts

def show_numbers(a,b,c):
    print("Positionals ", b,a,c)

show_numbers(1,2,3)
show_numbers(c= 30, a= 10, b=20)
show_numbers(a= 300, b= 100, c=300)

#Global and Local Veriables

count = 1
def change_count():
    print("Global Count: ",count)

#Parameter as local copy

def modify_number(num):
    num=10

x=5
modify_number(x)
print("Afterm modify number :", x)

#Recursiion
def factorial(n):
    if n == 1:  #base core
        return 1 
    return n * factorial(n=1)

print("Factorial of 5: ", factorial(5))

#Lambada Function

square = lambda x:x *x
print("Square using lambada ", square(4))
