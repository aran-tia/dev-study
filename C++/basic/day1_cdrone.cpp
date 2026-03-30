#include <iostream>
#include <string>
using namespace std;

int main() {
    int height = 0;
    int min_height = 0;

    for (int i = 0; i < 7; i++) {
        string cmd;
        cin >> cmd;

        if (cmd == "상승"){
            height += 1;
        }
        else if (cmd == "하강"){
            height -= 1;
        }
        if (height < min_height) {
            min_height = height;
        }
    }
    cout << min_height << endl;
    return 0;
}