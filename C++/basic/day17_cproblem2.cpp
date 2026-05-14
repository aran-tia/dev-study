#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;

    int arr[100];

    for (int i = 0; n > i; i++){
        cin >> arr[i];
    }
    for (int i = 0; n > i; i++){
        if (arr[i] % 2 == 0){
            cout << i << endl;
            break
        }
    int last = -1;
    for (int i = 0; n > i; i++){
        if (arr[i] % 2 == 0){
            last = i;
        }
    }
    }
    cout << last << endl;

    return 0;
}