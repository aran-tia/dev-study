#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    
    int arr[100];

    for (int i = 0; i < n; i++){
        cin >> arr[i]
    }

    int max_num = arr[i];
    int min_num = arr[i];

    for (int i = 1l i < n; i++ ){
        if (arr[i] > max_num){
            max_num = arr[i]
        }
        if (arr[i] < min_num){
            min_num = arr[i];
        }
    }

    cout << max_num << " " << min_num << endl;
    return 0;
}