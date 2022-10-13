class Human:
    leg_count = 4
    def get_gender(self, unknown):
        return unknown

class Man(Human):
    pass

class Woman(Human):
    pass


gender = Man()
print(gender.leg_count, gender.get_gender("Male"))

gender2 = Woman()
print(gender2.get_gender("Female"))
