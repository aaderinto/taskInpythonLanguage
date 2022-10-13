class Human:
    leg_count = 4
    can_walk = True

    def get_description(self, str):
        return str

    def get_leg_count(self, leg_count):
        return leg_count

tman = Human()
print(tman.leg_count)
print(tman.get_description("This is human"))
print(tman.get_leg_count(50), tman.can_walk)