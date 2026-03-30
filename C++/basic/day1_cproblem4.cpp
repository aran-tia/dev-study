#include <iostream>
using namespace std;

int main() {
    int max_num;
    cin >> max_num;

    for(int i = 0; i < 4; i++) {
        int x;
        cin >> x;

        if (x > max_num) {
            max_num = x;
        }
    }
    cout << max_num << endl;

    return 0;
}