#include <exception>
#include <string>
#include "Vehicle.cpp"

using namespace std;

class Car : public Vehicle {
public:
    void ChangeGear(Gear gear) override {
        if (Gear::R == gear && GetGear() == Gear::D) {
            string exception_msg = string("Can't change to REVERSE gear when ") + GetGearName(gear) + string(" gear is engaged!");
            throw exception(exception_msg.c_str());
        }
    }
};
