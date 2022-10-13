class Vechicle:
    model = "unknown"
    make = "unknown"
    production_year = "1990"

    def print_vechicle_info(self):
        print("\t The vechicle info is", self.model, self.make, self.production_year)


class car(Vechicle):
    wheel_count = 4
    def __init__(self, make, model):
        self.make = make
        self.model = model


car1 = car("Toyota", "Corolla")
print(car1.model)
car1.print_vechicle_info()


class plane(Vechicle):
    model = "Aeroplane"
    make = "Benz"

car2 = plane()
car2.print_vechicle_info()
