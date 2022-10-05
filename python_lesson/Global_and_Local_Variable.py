name = "Testify" #global variable
print(len(name))

def hello():
    lang = "Pyhton" #local variable
    print("Language is:",lang, name)

def greet():
    framework = "Selenium" #local variable
    print("Framework is:", framework, name)


hello()
greet()


def nn():
    name = "School"
    print(name) #Local variables shadows global variables

nn()