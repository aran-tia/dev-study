#include <iostream>
#include <string>
using namespace std;

int main() {
    int height = 0;
    int min_height = 0;

    while (true) {
        string cmd;
        cin >> cmd;

        if (cmd == "종료") {
            break;
        }
        else if (cmd == "상승") {
            height += 1;
        }
        if (height < min_height) {
            min_height = height;
        }
    }
    cout << "현재 높이: " << height << endl;
    cout << "최저 높이: " << min_height << endl;

    return 0;
}