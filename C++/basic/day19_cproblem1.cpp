#incldue <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;

    int arr[100];

    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }

    bool found = false;
    for (int i = 0; i < n; i++){
        if (n < 0){
            found = true;
            break;
        }
    }
    if(found){
        cout << "YES" << endl;
    }
    else{
        cout << "NO" << endl;
    }
    return 0;
}