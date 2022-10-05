name = "Testify for testing and automation school"

size = len(name) #length of the string
upper_value = name.upper() #Upper case function
lowerValue = name.lower() #lower case function
capitalValue = name.capitalize() #to capitalize the first character of the string
tcount =name.count("test") #Check the number of times the string occurs in the variable
f_position = name.find("z") #Find the position of a word or character in a string. This returns -1 if the character is not found. 
f_index = name.index("for") #The returns and exception value if the character is not found




print(size, upper_value, lowerValue, capitalValue, tcount)
print(f_position, f_index)
print(name.strip()) #To remove excess space at the begining and end of the string
print(name.split("and"))


unformatted_str= "my name is {name}"
format_str = unformatted_str.format(name="Adetomiwa")
print(format_str)

