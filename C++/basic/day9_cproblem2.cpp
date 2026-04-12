#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;

    int x;
    cin >> x;

    int sum = x;
    int max_num = x;
    int min_num = x;

    for (int i = 0; i < n - 1; i++){
        cin >> x;

        sum += x;

        if (x > max_num){
            max_num = x;
        }
        if (x < min_num){
            min_num = x;
        }
    }
    double avg = sum / (double)n;

    cout << avg << endl;
    cout << max_num << endl;
    cout << min_num << endl;

    return 0;
}