
import java.util.*;
import java.io.*;

class Q1
{
	public static void main (String[] args)
	{
		Scanner sc = new Scanner(System.in);
		Stack<String> stack = new Stack<String>(); //initalizing a stack
		
		int n = sc.nextInt();
		String arr[] = new String[n];
		for(int i=0;i<n;i++)
		    arr[i] = sc.next();
		
		int count = n;
		stack.push(arr[0]);
		
		for(int i=1;i<n;i++){
		    String a = stack.peek(); //peek operation
		    String b = arr[i];
		    if(a.equals(b)){
		        count -= 2;
		        String tmp = stack.pop(); //pop operation
		    }else
		        stack.push(arr[i]); //push operation
		}
		System.out.println(count);
	}
}
