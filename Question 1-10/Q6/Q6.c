#include <stdio.h>
int max(int arr[],int n,int l){
    int m=arr[n],i,pos;
    for(i=n;i<l;i++)
        if(m<=arr[i]){
            m=arr[i];
            pos=i;
        }
    return pos;
}
int main(){
    int i,arr[100],n,c=0;
    scanf("%d",&n);
    for(i=0;i<n;i++)
        scanf("%d",&arr[i]);
    for(i=0;i<n;i=max(arr,i,n)+1)
        c++;
    printf("%d",c);
    return 0;
}

