#include <iostream>
using namespace std;

int main() {
    int min_num;
    cin >> min_num;

    for (int i = 0; i < 4; i++) {
        int x;
        cin >> x;

        if (x < min_num) {
            min_num = x;
        }
    }
    cout << min_num << endl;

    return 0;
}