#include <iostream>
using namespace std;

int main(){
    int num;
    cin >> num;

    if (num > 0) {
        cout << "양수" << endl;
    }
    else if (num < 0) {
        cout << "음수" << endl;
    }
    else{
        cout << "0";
    }
    cout << num << endl;

    return 0; 

}