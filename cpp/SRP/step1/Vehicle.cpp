class Vehicle {
public:
	Vehicle(int maxFuel) {
		max_fuel_ = maxFuel;
		remaining_fuel_ = maxFuel;
	}

	// this is not a car's responsibility.
	void ReFuel() {
		remaining_fuel_ = max_fuel_;
	}

	int GetMaxFuel() {
		return max_fuel_;
	}

	int GetRemainingFuel() {
		return remaining_fuel_;
	}

	void SetRemainingFuel(int remaining_fuel) {
		remaining_fuel_ = remaining_fuel;
	}

	void Accelerate() {
		remaining_fuel_--;
	}

private:
	int max_fuel_;
	int remaining_fuel_;
};
