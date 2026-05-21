#include <iostream>
using namespace std;


int main(){
    int n;
    cin >> n;

    int arr[100];

    for(int i = 0; i < n; i++){
        cin >> arr[i;]
    }

    int max_num = arr[0];
    int max_num1 = arr[0];

    for (int i = 1; i < n; i++){
        if (arr[i] > max_num){
            max_num1 = max_num;
            max_num = arr[i];
        }
        else if (arr[i] > max_num1 && arr[i] != max_num){
            max_num1 = arr[i];
        }
    }

    cout << max_num << endl;
    cout << max_num1 << endl;

    return 0;

}