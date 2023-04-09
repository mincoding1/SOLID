#include "Vehicle.cpp"

class EventHandler {
public:
	EventHandler(Vehicle vehicle) {
		vehicle_ = vehicle;
	}

	void changeDrivingMode(DrivingMode driving_mode) {
		switch (driving_mode) {
			case DrivingMode::kSport: {
				vehicle_.SetPower(500);
				vehicle_.SetSuspensionHeight(10);
				break;
			}
			case DrivingMode::kComfort: {
				vehicle_.SetPower(400);
				vehicle_.SetSuspensionHeight(20);
				break;
			}
			default: {
				vehicle_.SetPower(400);
				vehicle_.SetSuspensionHeight(20);
				break;
			}
			// when we need to add another mode (e.g. ECONOMY) 2 classes will change DrivingMode and EventHandler.
		}
	}

private:
	Vehicle vehicle_;
};
