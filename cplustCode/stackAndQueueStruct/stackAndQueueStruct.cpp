#include<iostream>
#include<stack>
using namespace std;

bool isPopOrder(const int* pPush, const int* pPop, int length){
	bool bFlag = false;
	if(pPush != NULL && pPop != NULL && length > 0){
		const int* pNextPush = pPush;
		const int* pNextPop = pPop;
		std::stack<int>stackData;
		
		while(pNextPop- pPop < length){
			//当栈顶不是目标元素，再压入余下的元素,直到压到需要pop出去的元素为止。
			while(stackData.empty() || stackData.top() != *pNextPop){
				if(pNextPush - pPush == length) break; 
				stackData.push(pNextPush); // 压栈前，判定是否压完了。
				pNextPush++;
			}
			// 如果不是pop的元素，则退出，
			if(stackData.top() != *pNextPop) break;
			stackData.pop();
			pNextPop++;
		}
		if(stackData.empty() && pNextPop - pPop == length){
			bFlag = true;
		}
	}
	return bFlag;
}

int main(){
	
	const int nLength = 5;
	int ipush[nLength] = {1, 2, 3, 4, 5};
    	int pop1[nLength] = {4, 5, 3, 2, 1};
	int pop2[nLength] = {4, 3, 5, 1, 2};
	if (isPopOrder(ipush, pop1, nLength) == true)
		fprintf("pop1 Success!");
	else
		fprintf("pop1 Failed!");
	
	if (isPopOrder(ipush, pop2, nLength) == true)
		fprintf("pop2 Success!");
	else
		fprintf("pop2 Failed!");
	
	return 0;
}
