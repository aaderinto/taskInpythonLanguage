

print("Required Argument\n")
def add(num1, num2):
 print(num1 + num2)

add(2,3)

def greet(name):
    print("Hello", name)

greet("Tomiwa")

print("Default Argument\n")

def add(num1, num2=3):
    print(num1 + num2)

add(2)

def fullname(fName, lName="Aderinto"):
    print("My names are:", fName, lName)

fullname("Adetosin", "Fasawe") #For the default argument, if a new argument is passed it rides the default argument




print("Arbituary Argument\n")
def add(*args):
    print(args[0] + args[1])

add(2,3)

def resultSum(num1, num2):
    add = num1 + num2
    return add

sum = resultSum(10,6)
print(sum)