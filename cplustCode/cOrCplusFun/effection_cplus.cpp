#include<iostream>
#include<stdio.h>
class Base{
	private:
		int x;
	public:
		virtual void mf1()=0;
		virtual void mf1(int);
		virtual void mf2();
		void mf3();
		void mf3(double);
};


class Derived:public Base{
	public:
		void mf1(){
			printf("this is in Derived mf1.");
		};
		void mf3(){
			printf("this is in Derived mf3.");
		};
		void mf4(){
			printf("this is in Derived mf4.");

		};
};

int main(){
	Derived d;
	int x;

	d.mf3();
//	d.mf1(x);

	return 0;
}




