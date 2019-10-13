#include <stdio.h>
#include <stdlib.h>
int findSingle(int * arr, int n){
    int i, res = 0;
    for(i=0;i<n;i++)
        res = res ^ arr[i];
    return res;
}

int main(void){
    int n, *arr, i;
    scanf("%d", &n);
    arr = (int *)malloc(n*sizeof(int));

    for(i=0;i<n;i++)
        scanf("%d", &arr[i]);

    printf("%d\n", findSingle(arr, n));
    return 0;
}
