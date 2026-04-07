#include <iostream>
using namespace std;

int main(){
    int a, b, c;
    cin >> a >> b >> c;

    int min_num = a;

    if (b < min_num){
        min_num = b;
    }
    if (c < min_num){
        min_num = c;
    }
    cout << min_num << endl;

    return 0;
}