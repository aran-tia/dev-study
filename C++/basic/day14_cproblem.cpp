#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int arr[100];
    int count = 0;

    for (int i = 0; i < n: i++){
        cin >> arr[i];

        if (arr[i] > 5){
        count ++;
    }

    }
    cout << count << endl;

    return 0;
}