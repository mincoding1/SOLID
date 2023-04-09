class RacingCar {
public:
    RacingCar(int max_fuel) {
        max_fuel_ = max_fuel;
        remaintning_fuel_ = max_fuel;
    }

    void Accelerate() {
        power_++;
        remaintning_fuel_--;
    }

private:
    int max_fuel_;
    int remaintning_fuel_;
    int power_;
};
