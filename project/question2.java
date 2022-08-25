import java.util.*;
import java.lang.*;
public class question2 {
    public static int factorial(int n)
    {
        if (n == 0)
            return 1;
        return n*factorial(n-1);
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int s1=0;
        int e=1,d=2;
        System.out.println("Enter the value of n");
        int n=sc.nextInt();
        System.out.println("Enter the value of m");
        int m=sc.nextInt();
        System.out.println("Enter the value of a");
        int a=sc.nextInt();

        int fibo[]=new int[n+1];
        fibo[0] = 0; fibo[1] = 1;
        int s2 = fibo[0] + fibo[1];
        for (int i=2; i<=n; i++)
        {
            fibo[i] = fibo[i-1]+fibo[i-2];
            s2 += fibo[i];
        }
        System.out.println(s2);
        for(int i=1;i<=n;i++){
            if (i%2==0){
                s1-=(Math.pow(a,e))/factorial(d);
            }
            else{
                s1+=(Math.pow(a,e))/factorial(d);
            }
            e+=3;
            d+=2;
        }
        System.out.println(s1+s2);
    }
}
