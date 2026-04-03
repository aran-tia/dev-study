#include <iostream>
using namespace std;

int main(){
    
    int sum;
    cin >> sum;

    int max_num = sum;

    int min_num = sum;

    for(int i = 0; i < 4 ; i++){
        int x;
        cin >> x;

        sum += x;

        if (x > max_num){
            max_num = x;
        }
        if (x < min_num){
            min_num = x;
        }
    }

    double avg;
    avg = sum / 5.0;
    cout << avg << endl;
    cout << max_num << endl;
    cout << min_num << endl;

    return 0;
}