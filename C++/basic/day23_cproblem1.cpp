#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int arr[100];

    for (int i = 0; i < n; i++){
        cin >> arr[i];
    }

    bool found = false;

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            if (arr[i] == arr[j]){
                found = true;
                break;
            }
            }
        }
    

    if (found){
        cout << "YES" << endl;
    }
    else{
        cout << "NO" << end;
    }
    return 0;
}