#include <string>

using std::string;

class Greeter {
public:
	string Greet() {
		if (formality_ == "formal") {
			return "Good evening, sir.";
		}
		else if (formality_ == "casual") {
			return "Sup bro?";
		}
		else if (formality_ == "intimate") {
			return "Hello Darling!";
		}
		else {
			return "Hello.";
		}
	}

	void SetFormality(string formality) {
		formality_ = formality;
	}

private:
	string formality_;
};
