#include <stdio.h>
#include <stdlib.h>

/*solution explaination:
	We keep the track of balance of the string i:e the number of ‘(‘ minus the number of ‘)’.
	A string is valid if its balance is 0, and also every prefix has non-negative balance.

	Now, consider the balance of every prefix of S. If it is ever negative (say, -1),
	we must add a ‘(‘ bracket at the beginning. Also, if the balance of S is positive (say, +P),
	we must add P times ‘)’ brackets at the end.
*/

int checkparenthesis(char * str, int size){
	int i, bal=0;
	for(i=0;i<size;i++)
		bal += str[i]=='('?1:-1;
	return bal;
}

int main(void){
	char *str, size, i, ans;

	/*input*/
	printf("enter the size of the string - ");
		scanf("%d",&size);
	str =  (char *)malloc(sizeof(size));
	printf("enter the string - ");
		scanf("%s", str);

	/*bracket fix*/
	ans = checkparenthesis(str,size);
	ans = ans>=0?ans:-1*ans;

	/*output*/
	printf("%d\n",ans);
	return 0;
}