#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define MAX 15 //stack size

//Stack declaration
char stack[MAX][20];
int top = -1;
int isFull(){
	return top==MAX-1;
}
void push(char str[]){
	if(isFull()){
		printf("Stack Overflow");
		exit(0);
	}else
		strcpy(stack[++top],str);
}

int main(void){
	char arr[MAX][20];
	int n, i, count;
	
	//inputs
	scanf("%d",&n);
	for(i=0;i<n;i++)
		scanf("%s", arr[i]);
		
	//main code starts here	
	count = n;
	push(arr[0]);	
	for(i=1;i<n;i++){
		if(strcmp(stack[top],arr[i])==0){
			top--; //pop operation
			count-=2;
		}else
			push(arr[i]); //push operation
	}
	
	//output
	printf("%d",count);
	return 0;
}
