#This talks about abstract class and attributes when you don't want to reveal some information
class loginDetails:
    _email= "ade@gmail.com"
    _password= "Admin1234"

    def get_email(self):
        return self._email

    def get_password(self):
        return "**********"

loginDetails = loginDetails()
print(loginDetails.get_email())
print(loginDetails.get_password())
