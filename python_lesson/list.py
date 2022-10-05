language = ["python","java","cSharp","goLang","java"]
language.append("JavaScript") #adds a value to the end of the list
language.insert(3, ".Net") #to add a value to any position you desire in the list
language.pop(4) #to remove by index
language.remove("cSharp") #to remove by value


print(language)
language.sort(reverse=True) # to sort in descending order
language_copy = language.copy() # to copy the value in a new variable
print(language_copy)
language.reverse() # to print the list value in reverse order
print(language)
print(language.count("java")) #to count the number of occurence in a list. 
print(len(language)) #to count the length of items in a list
print(language.clear())
print(len(language))