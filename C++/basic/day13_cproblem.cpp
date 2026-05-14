#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;


    int arr[100];
    int sum = 0;

    for (int i = 0; i < n; i++){
        cin >> arr[i];
        
        if(arr[i] % 2 == 1){
            sum += arr[i];
        } 
    }
    
    cout << sum << endl;

    return 0;
}