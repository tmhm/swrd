#include<iostream>
#include<stdio.h>


using namespace std;
typedef struct{

    double d1;
    char ch1;
//    int i2;
    short s2;
    char ch3;
//    short s1;
//    short s3;
    int i1;
//    char ch2;
}test;
typedef struct{
    int a;
    //char c1;

    short s1;
    char c2;
    char c3;
//    short s2;
}test1;

#pragma pack(2)
class BU{
     int number;
     union UBffer{
         char buffer[13];
         int number;
     }ubuf;
     void foo(){}
     typedef char*(*f)(void*);
     enum{hdd,ssd,blueray}disk;
     int* a;
}bu;
#pragma(4)

int main(){
    cout << sizeof(bu) << endl;
    std::cout << sizeof(test) << std::endl;

    cout << sizeof(long) << endl;
    int ret = sizeof(test1);
    printf("out : %d \n\n", ret);
    return 0;
}
