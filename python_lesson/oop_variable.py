#class
class Animal:
    group = "Mammals"
    can_walk =  True #class variable

    def __init__(self, name): #A constructor is a code use to initialize the class
        self.name = name #instance variable

    def get_group(self):
        return self.group

cat = Animal("Cat")
dog = Animal("Dog")

#print(cat.name)
#print(dog.name)
#print(dog.group)

lion = Animal("lion")
print(lion.get_group())