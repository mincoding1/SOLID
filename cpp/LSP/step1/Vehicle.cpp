#pragma once
#include <string>

enum class Gear {
	P, //Parking
	R, //Reverse
	N, //Neutral
	D, //Drive
};

class Vehicle {
public:
	Gear GetGear() {
		return gear_;
	}

	virtual void ChangeGear(Gear gear) {
		gear_ = gear;
	}

	std::string GetGearName(Gear gear) {
		if (gear == Gear::P) return "Parking";
		if (gear == Gear::R) return "Reverse";
		if (gear == Gear::N) return "Neutral";
		if (gear == Gear::D) return "Drive";
	}

private:
	Gear gear_;
};
