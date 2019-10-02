#include<stdio.h>
#include<stdlib.h>
void findrange(int * arr, int low, int high){
	int i, min = arr[low], max = arr[low], pos1 = low, pos2 = low;
	if(low==high){
		printf("%d\n",-1); // if the list is already sorted
		return;
	}
	for(i=low;i<=high;i++){
		if(min>arr[i]){
			min = arr[i];
			pos1 = i; //index of min
		}
		if(max<=arr[i]){
			max = arr[i];
			pos2 = i; //index of max
		}
	}
	if(pos1==low && pos2 == high)
		findrange(arr, low+1, high-1);
	else if(pos1==low)
		findrange(arr, low+1, high);
	else if(pos2==high)
		findrange(arr, low, high-1);
	else
		printf("%d %d\n",low, high);
}
int main(void){
	int * arr, n, i;
	// input
	scanf("%d",&n);
	arr = (int*)malloc(n*sizeof(int));
	for(i=0;i<n;i++)
		scanf("%d",&arr[i]);
	// recursive solution	
	findrange(arr, 0, n-1);
	return 0;
}
