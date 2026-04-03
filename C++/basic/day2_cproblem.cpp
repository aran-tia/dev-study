#include <iostream>
using namespace std;

int main(){
    int sum_number;
    cin >> sum_number;

    for(int i=0; i< 4; i++){
        int x;
        cin >> x;
        sum_number += x;
    }

    cout << sum_number << endl;

    return 0;


}