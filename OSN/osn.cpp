#include <iostream>
using namespace std;

int main() {
    int a, b, c, d, x;
    a = 1; b = 2; c = 3; d = 5;
    cout <<a<<b<<c<<d;

    a = a + a;
    b = a + b;
    c = a + b + c;
    d = a + b + c + d;
    x = a + b + c + d;
    cout << "X =" << x << endl;
}