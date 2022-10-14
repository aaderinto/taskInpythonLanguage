class Human:
    leg_count = 4
    def get_gender(self):
        return "unknown"

class Man(Human):
    pass

class Woman(Human):
    pass


gender = Man()
print(gender.leg_count, gender.get_gender())

gender2 = Woman()
print(gender2.get_gender())
