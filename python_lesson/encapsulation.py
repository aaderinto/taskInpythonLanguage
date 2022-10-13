class user:
    _fName = "Adetomiwa"
    _lname = "Aderinto" #how to declare a variable that you don't want to be accessed
    _attendancee = 1

    def get_name(self):
        return self._fName

    def get_attendance(self):
        value = self._attendancee * 20
        return value

user = user()
print(user.get_name())
print(user.get_attendance())