#incldue <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;

    int arr[100];
    int even = 0;
    int odd = 0;

    for (int i = 0; i < n; i++){
        cin >> arr[i];

        if (arr[i] % 2 == 0){
            even++;
        }
        else if (arr[i] % 2 == 1){
            odd++; 
        }
    }
    cout << even << "" << odd << endl;

    return 0;
}