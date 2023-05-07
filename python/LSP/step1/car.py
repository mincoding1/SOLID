from vehicle import Vehicle, Gear

class Car(Vehicle):
    def change_gear(self, gear: Gear):
        if Gear.R == gear and self.get_gear() == Gear.D :
            exception_msg = 'Can\'t change to REVERSE gear when ' + self.get_gear_name(gear) + ' gear is engaged!'
            raise Exception(exception_msg)
        super().change_gear(gear)
