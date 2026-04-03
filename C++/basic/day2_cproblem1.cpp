#include <iostream>
using namespace std;

int main(){
    int average_number;
    cin >> average_number;
    int sum;
    cin >> sum;

    for(int i = 0; i < 4; i++){
        int x;
        cin >> x;
        sum += x;

    }

    double avg;
    avg = sum / 5

    cout << avg << endl;

    return 0;
}