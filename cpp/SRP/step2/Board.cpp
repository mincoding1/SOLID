#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Board {
public:
    Board() {
        for (int i = 0; i < 9; i++) {
            spots_.push_back(to_string(i));
        }
    }

    vector<string> FirstRow() {
        vector<string> first_row;
        first_row.push_back(spots_[0]);
        first_row.push_back(spots_[1]);
        first_row.push_back(spots_[2]);
        return first_row;
    }

    vector<string> SecondRow() {
        vector<string> second_row;
        second_row.push_back(spots_[3]);
        second_row.push_back(spots_[4]);
        second_row.push_back(spots_[5]);
        return second_row;
    }

    vector<string> ThirdRow() {
        vector<string> third_row;
        third_row.push_back(spots_[6]);
        third_row.push_back(spots_[7]);
        third_row.push_back(spots_[8]);
        return third_row;
    }

    void Display() {
        string formatted_first_row = spots_[0] + " | " + spots_[1] + " | " + spots_[2] + "\n" + spots_[3] + " | " + spots_[4] + " | " + spots_[5] + "\n" + spots_[6] + " | " + spots_[7] + " | " + spots_[8];
        cout << formatted_first_row << "\n";
    }

private:
    vector<string> spots_;
};
