import java.util.*;

public class question3 {
    public static int factorial(int n)
    {
        if (n == 0)
            return 1;
        return n*factorial(n-1);
    }

    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the number");
        int n=sc.nextInt();
        int m=n;
        int dig;
        int s=0,h=0;
        while (m!=0){
            dig=m%10;
            m/=10;
            s+=factorial(dig);
            h+=dig;
        }
        if (s==n){
            System.out.println("It is a special number");
        }
        else{
            System.out.println("It is not a special number");
        }
        if (n%h==0){
            System.out.println("It is a Harshad number");
        }
        else{
            System.out.println("It is not a harshad number");
        }
    }
}
