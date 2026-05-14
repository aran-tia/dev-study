#incldue <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int arr[100];

    for (int i = 0; i < n; i++){
        cin >> arr[i];
    }
    int min_index = 0;

    for (int i = 0; i < n; i++){
        if (arr [i] < arr[min_index]){
            min_index = i;
        }

    }
    cout << min_index << endl;

    return 0;
}