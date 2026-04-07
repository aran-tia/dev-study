#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    if (a > b) {
        cout << a << endl;
    }
    else if (a < b) {
        cout << b << endl;
    }
    else {
        cout << "같음" << endl;
    }
    return 0;
}