#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;

    int arr[100];

    for (int i = 0; i < n; i++){
        cin >> arr[i];
    }

    int max_index = 0;
    int min_index = 0;

    for (int i = 0; i < n; i++){
        if (arr[i] > arr[max_index]){
            max_index = i;
        }
        if (arr[i]) < arr[min_index]{
            in_index = i
        }
    }
    cout << max_index << endl;
    cout << min_index << enld;

    return 0;
}