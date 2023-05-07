#include <iostream>
#include <string>
#include "Phone.cpp"
#include "Emailer.cpp"
using namespace std;

class WeatherTracker {
	WeatherTracker() {
	}

	void SetCurrentConditions(string weather_description) {
		current_conditions_ = weather_description;
		if (weather_description == "rainy") {
			string alert = phone_.GenerateWeatherAlert(weather_description);
			cout << alert << "\n";
		}
		if (weather_description == "sunny") {
			string alert = emailer_.GenerateWeatherAlert(weather_description);
			cout << alert << "\n";
		}
	}

private:
	string current_conditions_;
	Phone phone_;
	Emailer emailer_;
};
