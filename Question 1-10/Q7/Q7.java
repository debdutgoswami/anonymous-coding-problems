import java.util.*;
public class Q7
{
    int findSingle(int arr[])
    {
        int res = 0;
        for(int i=0;i<arr.length;i++)
            res = res ^ arr[i];
        return res;
    }
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        Q7 obj = new Q7();
        int n = sc.nextInt();
        int arr[] = new int[n];
        for(int i=0;i<n;i++)
            arr[i] = sc.nextInt();
            
        System.out.println(obj.findSingle(arr));
    }
}
