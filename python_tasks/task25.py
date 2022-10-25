from collections import namedtuple


class Utilities:
    @staticmethod
    def print_name(name):
        return name

    def print_nam(name):
        return name

print(Utilities.print_name("Adetomiwa"))

Utilities.print_nam = staticmethod(Utilities.print_nam)
print(Utilities.print_nam("Aderinto"))
