import java.util.*;
public class Q2
{
    public static void findrange(int arr[], int low, int high){
        if(low==high){
            System.out.println(-1);
            return;
        }
        int min = arr[low], max = arr[low], pos1 = low, pos2 = low;
        for(int i=low;i<=high;i++){
            if(max<=arr[i]){
                max=arr[i];
                pos2=i;
            }
            if(min>arr[i]){
                min=arr[i];
                pos1=i;
            }
        }
        if(pos1==low && pos2==high)
            findrange(arr,low+1,high-1);
        else if(pos1==low)
            findrange(arr, low+1, high);
        else if(pos2==high)
            findrange(arr,low,high-1);
        else
            System.out.println(low+" "+high);
    }
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        Q2 obj = new Q2();
        int n;
        n = sc.nextInt();
        int arr[] = new int[n];
        for(int i=0;i<n;i++)
            arr[i] = sc.nextInt();
            
        obj.findrange(arr,0,n-1);
    }
}
