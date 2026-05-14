#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;

    int arr[100];

    for (int i = 0; i < n; i++){
        cin >> arr[i];
    }

    int min_num = arr[0];

    for (int i = 0; i < n; i++){
        if (arr[i] == min_num){
            min_num = arr[i];
        }
    }

    int count = 0;
    
    for (int i = 0; i < n; i++){
        if (arr[i] == min_num){
            count++;
        }
    }
    cout << count << endl;

    return 0;
}