class Human:
    leg_count = 4
    def get_gender(self, unknown):
        return unknown

class man(Human):
    def get_gender(self, gender):
        return gender

class woman(Human):
    def get_gender(self, unknown):
        return super().get_gender(unknown)



m_gender = man()
print(m_gender.get_gender("Male"))

w_gender = woman()
print(w_gender.get_gender("Female"))