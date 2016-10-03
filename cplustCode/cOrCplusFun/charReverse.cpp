#include<iostream>
using namespace std;

int myStrLen(const char *str){
	int ret = 0;
	if(str != NULL){
		while(*str != '\0'){
			ret++;
			str++;
		}
	}
	return ret;
}
void CharReverse(char* pch,int index, int length){
	if(index < length/2){
		char tmp = *(pch+index);
		*(pch + index) = *(pch + length - (index+1));
		*(pch + length - (index+1)) = tmp;
		cout << tmp << endl;
		CharReverse(pch, ++index, length);
	}
	else{
		return ;
	}
}
int main(){
	char cp[] = "This is a test!";
	cout << cp << endl;
	int ilen = 0;
	ilen = myStrLen(cp);
	cout << ilen << endl;
	ilen = strlen(cp);
	cout << ilen << endl;
	int sp = 0; 
	CharReverse(cp, sp, ilen);

	cout << cp << endl;
	return 0;		
}

