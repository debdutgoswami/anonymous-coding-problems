# include<stdio.h>

int main(void){
    int n;
    scanf("%d", &n);

    for (int i=1;i<n;i++){
        for (int j=n;j>i;j--)
            printf(" ");
        printf("/");
        for (int j=1;j<=(2*i-2);j++)
            if (i%2==0)
                printf("-");
            else
                printf("=");
        printf("\\\n");
    }
    printf("<");
    for (int i=1;i<=(2*n-2);i++)
        if (n%2==0)
            printf("-");
        else
            printf("=");
    printf(">\n");
    for (int i=n-1;i>=1;i--){
        for (int j=n;j>i;j--)
            printf(" ");
        printf("\\");
        for (int j=1;j<=(2*i-2);j++)
            if (i%2==0)
                printf("-");
            else
                printf("=");
        printf("/\n");
    }

    return 0;
}