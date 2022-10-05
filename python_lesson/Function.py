print("function\n")

def greetings():
    print("Hello World from Python")

greetings()

def goodBye():
    print("Good Bye Python")

goodBye()

def ValidateKeys():
    pass

ValidateKeys() #This is an empty function


print("Anonymous Function\n")

anGreet = lambda : print("Hello World from Python Anonymously")
anGreet()


sum = lambda x, y: x + y
print(sum(5,6))