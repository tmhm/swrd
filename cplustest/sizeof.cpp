#include<iostream>
using namespace std;
int main(){

    cout << "char: " << sizeof(char) << endl;
    cout << "short: " << sizeof(short) << endl;
    cout << "int: " << sizeof(int) << endl;
    cout << "long: " << sizeof(long) << endl;
    cout << "unsigned long: " << sizeof(unsigned long) << endl;
    cout << "long long: " << sizeof(long long) << endl;
    //在vc6.0下不支持 long long 数据类型。
    cout << "double: " << sizeof(double) << endl;
    cout << "char*: " << sizeof(char*) << endl;
    return 0;
}
