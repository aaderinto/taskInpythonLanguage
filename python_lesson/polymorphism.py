class vechicle:
    def drive_direction(self):
        print("This can drive backward")

class plane(vechicle):
    def drive_direction(self):
        print("This can drive forward")

class submarine(vechicle):
    pass

vechicle = vechicle()
vechicle.drive_direction()

plane = plane()
plane.drive_direction()

bicycle = submarine()
bicycle.drive_direction()