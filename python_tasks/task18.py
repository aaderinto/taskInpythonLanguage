class Human:
    leg_count = 4
    can_walk = True


cat = Human()
print(cat.can_walk)
print(cat.leg_count)

class iHuman:
    def __init__(self,leg_count,can_walk):
        self.leg_count = leg_count
        self.can_walk = can_walk

dog = iHuman(4, True)
print(dog.leg_count, dog.can_walk)