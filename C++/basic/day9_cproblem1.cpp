#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    int min_num;
    cin >> min_num;

    for (int i = 0; i < n-1; i++){
        int x;
        cin >> x;

        if (n < min_num){
            min_num = x;
        }
    }
    cout << min_num << endl;

    return 0;
}