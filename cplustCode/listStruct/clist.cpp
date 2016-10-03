#include<iostream>
#include<stack>
using namespace std;

struct ListNode{
	int m_nValue;
	ListNode* m_pNext;
};

void AddToTail(ListNode** pHead, int value){
	ListNode* pNew = new ListNode();
	pNew->m_nValue = value;
	pNew->m_pNext = NULL;
	if (*pHead == NULL){
		*pHead = pNew;
	}
	else{
		ListNode* pNode = *pHead;
		while(pNode->m_pNext != NULL){
			pNode = pNode->m_pNext;
		}
		pNode->m_pNext = pNew;
	}
}

void RemoveNode(ListNode** pHead, int value){
	if(pHead == NULL || *pHead == NULL)
		return;
	ListNode* pToBeDeleted = NULL;
	if((*pHead)->m_nValue == value){
		pToBeDeleted = *pHead;
		*pHead = (*pHead)->m_pNext;
	}
	else{
		ListNode* pNode = *pHead;
		while(pNode->m_pNext != NULL 
				&& pNode->m_pNext->m_nValue != value)
			pNode = pNode->m_pNext;
		if(pNode->m_pNext != NULL && pNode->m_pNext->m_nValue == value){
			pToBeDeleted = pNode->m_pNext;
			pNode->m_pNext = pNode->m_pNext->m_pNext;
		}
	}
	if(pToBeDeleted != NULL){
		delete pToBeDeleted;
		pToBeDeleted = NULL;
	}
}

ListNode* ReverseList(ListNode* pHead){
	if(pHead == NULL || pHead->m_pNext ==NULL){
		return pHead;
	}else{
		ListNode* newHead = ReverseList(pHead->m_pNext);
		pHead->m_pNext->m_pNext = pHead;
		pHead->m_pNext = NULL;
		return newHead;
	}
}

void printList(ListNode* pHead){
	ListNode* p = pHead;
	while(p != NULL){
		//cout<< p->m_nValue<< endl;
		printf("%d\t", p->m_nValue);
		p = p->m_pNext;
	}
	printf("\n");
}


void PrintListReversingly(ListNode* pHead){
	std::stack<ListNode*> nodes;
	ListNode* pNode = pHead;
	while(pNode != NULL){
		nodes.push(pNode);
		pNode = pNode->m_pNext;
	}
	while(!nodes.empty()){
		pNode = nodes.top();
		printf("%d\t", pNode->m_nValue);
		nodes.pop();
	}
	printf("\n");
}


void PrintListReversingly_recursively(ListNode* pHead){
	if(pHead != NULL){
		if(pHead->m_pNext != NULL){
			PrintListReversingly_recursively(pHead->m_pNext);
		}
		printf("%d\t",pHead->m_nValue);
	}
//	printf("\n");
}

int main(){
	ListNode* test = new ListNode();
	test->m_nValue = 0;
	int numOfNodeAdd = 10;
	for(int i = 1; i <= numOfNodeAdd ; ++i){
		AddToTail(&test, i);	
	}
//	AddToTail(&test, 5);	
//	AddToTail(&test, 6);
//	AddToTail(&test, 7);
	printList(test);
	test = ReverseList(test);
	printList(test);
//	PrintListReversingly(test);
//	PrintListReversingly_recursively(test);
	printf("\n");
}
