#include "racing_car.cpp"

class Pilot {
public:
    Pilot() {
        vehicle_ = new RacingCar(100);
    }

    void IncreaseSpeed() {
        vehicle_->Accelerate();
    }

private:
    RacingCar *vehicle_;
};
