#pragma once
#include "Vehicle.cpp";

class Drone : public Vehicle {
public:
	bool IsCameraOn() {
		return camera_on_;
	}

	void TurnCameraOn() override {
		camera_on_ = true;
	}

	void TurnCameraOff() override {
		camera_on_ = false;
	}

	void TurnRadioOn() override {
		// nothing to do here
	}

	void TurnRadioOff() override {
		// nothing to do here
	}

private:
	bool camera_on_;
};
