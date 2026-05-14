#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int arr[100];

    for (int i = 0; i < n; i++){
        cin >> arr[i];
    }
    bool ok = true;

    for (int i = 0; i < n; i++){
        if (arr[i] > arr[i - 1]){
            ok = false;
        }
    }

    if (ok){
        cout << "YES" << endl;
    }
    else{
        cout << "NO" << endl;
    }

    return 0;
}