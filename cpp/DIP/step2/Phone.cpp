#include <string>
using namespace std;

class Phone {
public:
	string GenerateWeatherAlert(string weather_conditions) {
		string alert = "It is " + weather_conditions;
		return alert;
	}
};