#include <string>
using namespace std;

class Emailer {
public:
	string GenerateWeatherAlert(string weather_conditions) {
		string alert = "It is " + weather_conditions;
		return alert;
	}
};
