#include <iostream>
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

typedef struct{

}test_null;

typedef struct{
	double d1;
	char c1;
	short s1;
	char ch2;
	int i1;
}testdouble;

typedef struct{
	int d1;
	char c1;
	short s1;
	char ch2;
	int i1;
}testint;

#pragma pack(2)
typedef struct{
	int d1;
	char c1;
	short s1;
	char ch2;
	int i1;
}testint2; 
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

#pragma pack(1) //将地址对齐界限设置为1的整数倍
 typedef struct {
	char ch1;
	char ch2;
	int n;
	char ch3;
}stch3_1;

class clt_1{
	char ch1;
	int a;
	short b;
	char c;
	stch3_1 st1;
}st_inside;
#pragma pack(4) //将地址对齐界限设置为4的整数倍



typedef struct {
	//int a;    //4
	double a;
	short b;  //2
	char c;   //1
} stlt;    // 8

class clt{
	char ch1;  //4
	int a;     // 4
	short b;   // 2
	char c;    //1

	stlt s;   // 8
};       //20

class clt2{
	stlt s;   // 8   // 否决掉并不是按最大基本类型 8 来进行递归的！
						//http://www.cnblogs.com/biyeymyhjob/archive/2012/09/07/2674992.html   有误
	char ch1; // 4
	//int a;    //4
	//int a2;   //4
	//char ch2;

	//short b;
	//char c;
};



typedef struct {
	char ch1;
	char ch2;
	int n;
	char ch3;
} stch3;




int main(int argc, char** argv) {

	clt A;
	clt2 A2;
	stlt B;

	stch3 C;
	stch3_1 D;
	clt_1 E;

	//clt *ct = new clt();
	int i = sizeof(int);
	int l = sizeof(short);
	int c = sizeof(char);

	//int lc = sizeof(clt);
	//int ls = sizeof(stlt);
	int ctc = sizeof(A);
	int cts = sizeof(B);
	int ctc2 = sizeof(A2);

	int ct3 = sizeof(C);
	int ct3_2 = sizeof(D);
	int ctc_2 = sizeof(E);

	cout << "test null struct: " << sizeof(test_null) << endl;
	cout << "sizeof(bu): " << sizeof(bu) << endl;
	cout << "sizeof(testdouble):" << sizeof(testdouble) << endl;
	cout << "sizeof(testint):" << sizeof(testint) << endl;
	cout << "sizeof(testint2):" << sizeof(testint2) << endl;
	cout << "st_inside: " << sizeof(st_inside) << ",  inside stch3_1: "<< sizeof(stch3_1) << endl;
	cout << endl;

	//printf("sizeof(int, short, char): %d, %d, %d . \n\n", i,l,c);
	/*
	cout << "char: " << sizeof(char) << endl;
	cout << "short: " << sizeof(short) << endl;
	cout << "int: " << sizeof(int) << endl;

	cout << "long: " << sizeof(long) << endl;
	cout << "unsigned long: " << sizeof(unsigned long) << endl;
	cout << "long long: " << sizeof(long long) << endl;
	cout << "double: " << sizeof(double) << endl;
	cout << "char*: " << sizeof(char*) << endl;
	cout << endl;
	*/
	//printf("sizeof(class): %d ,\n sizeof(struct): %d \n",lc,ls);
	//printf("sizeof(struct): %d \n",ls);
	//printf("sizeof(class instance ): %d,\n sizeof(struct instance): %d \n",ctc,cts);
	//printf("sizeof(class instance): %d \n\n",ctc2);

	//printf("sizeof(struct instance stch3): %d \n",ct3);
	//printf("\n.After change pack to '1'. \n");

	//printf("sizeof(struct instance stch3, clt_1): %d , %d \n\n",ct3_2, ctc_2);

//	system("pause");

	return 0;
}

