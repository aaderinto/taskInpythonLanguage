#1 Create a two string variable, concatenate the two variable and print out the results

def cont_str(a, b):
    print(a + b)

print("********* Ans to Question 1 ************")
cont_str('inte', 'gration')

#2 Create a function that calculates the power of a number. 
# Then write a unit test to check the correctness of the function. 

def powerN():
    pass



#3 Using the OOP feature Inheritance, 
# create a class Animal withthe method sound() 
# and then create a Cat and Dog class thatinherits from the Animal class. 
# The Cat and Dog class shouldoverride the sound class and print a different sound.


class Animal:
    def sound(self):
        a_sound = "No sound"
        return a_sound

class Cat(Animal):

    def sound(self):
        a_sound = "This sound"
        return a_sound
    

class Dog(Animal):

    def sound(self):
        a_sound = "Dog sound"
        return a_sound


current_cat_sound = Cat()
current_dog_sound = Dog()
print("********* Ans to Question 2 ************")
print(current_cat_sound.sound())
print(current_dog_sound.sound())

#4 Writing  a  well-documented  code  creates  a  function  
# thatcalculates simple interest

def simpleIntrest(P, R, T):
    I = P * R * T
    return I

get_simpleInterest = simpleIntrest(10, 0.5, 4)
print("********* Ans to Question 4 ************")
print(get_simpleInterest)


#6.  Write  a  function  that  removes  repeated  charactersfrom a string. 
# Sample Strings are: 
# a. Hello: output shouldbe Helo 
# b. Concatenate: output should be Conaten

def remove_repeated_characters(strr):
    sta = ""
    for i in strr:
        if (i not in sta.casefold() ):
            sta += i
    print(sta)

print("********* Ans to Question 6 ************")
remove_repeated_characters('Hello')
remove_repeated_characters('Concatenate')

print("********* Ans to Question 7 ************")
#7. Create a program that prints out the odd numbers in anarray. 
# Sample array: a. [1, 2, 3, 4, 5, 6] b. [ 34, 2, 9, 91, 19,401, 0 ]

def printOddNumbers(arr):
    j = []
    for i in arr:
        if i % 2 != 0:
            j.append(i)
    print(j)
            
arr = [1,2,3,4,5,6]
arrr = [34,2,9,91,19,401,0]
printOddNumbers(arr)
printOddNumbers(arrr)

print("********* Ans to Question 8 ************")
#8. Create a program that prints out the even numbers inan array. 
# Sample array: a. [1, 2, 3, 4, 5, 6] b. [ 34, 2, 9, 91, 19,401, 0 ]

def printEvenNumbers(arr):
    j = []
    for i in arr:
        if i % 2 == 0:
            j.append(i)
    print(j)
            
arr = [1,2,3,4,5,6]
arrr = [34,2,9,91,19,401,0]
printEvenNumbers(arr)
printEvenNumbers(arrr)

print("********* Ans to Question 9 ************")
# 9.  Create  a  function  that  converts  any  string  value  to  uppercase,  
# Then  write  a  unit  test  that  checks  the  function'scorrectness.
def upperStringConversion(ustr):
    return ustr.upper()

print("********* Ans to Question 10 ************")
# 10. Create a function that converts any string value to aSentence  case,  
# Then  write  a  unit  test  that  checks  thefunction's correctness.

def sentenceCase(ustr):
    return (ustr.capitalize(), ustr.swapcase())
    