#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;

    int arr[100];
    int max_num = -1;

    for (int i = 0; i < n; i++){
        cin >> arr[i];

        if (arr[i] % 2 == 0 && arr[i] > max_num){
            max_num = arr[i]
        }
    }

    cout << max_num << endl;

    return 0;
}