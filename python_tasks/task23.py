class User:
    _password = "password"

    def get_password(self):
        return "**********"

class ActiveUser(User):
    def get_password(self):
        return "*********"

passwd = ActiveUser()
print(passwd.get_password())
