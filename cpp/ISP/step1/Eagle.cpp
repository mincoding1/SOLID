#include <string>
#include "Bird.cpp";
using namespace std;

class Eagle : public Bird {
public:
    Eagle(int initial_feather_count) {
        number_of_feathers_ = initial_feather_count;
    }

    void Fly() override {
        current_location_ = "in the air";
    }

    void Molt() override {
        number_of_feathers_ -= 1;
    }

private:
    string current_location_;
    int number_of_feathers_;
};