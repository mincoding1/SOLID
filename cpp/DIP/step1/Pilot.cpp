#include "RacingCar.cpp"

class Pilot {
public:
    Pilot() {
        vehicle_ = RacingCar(100);
    }

    void IncreaseSpeed() {
        vehicle_.Accelerate();
    }

private:
    RacingCar vehicle_;
};
