
#class
class Animal:
    name = "Cow"
    group = "Mammals"

    def get_name_group(self):
        return self.name + ":" + self.group

#Object: This is an instance of a class

output = Animal() #Creating an instance of a class

print(output.name, output.group, output.get_name_group())