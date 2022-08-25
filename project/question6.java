import java.util.*;
public class question6 {

    long n;
    void input(){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the value of n");
        n=sc.nextLong();
    }

    static long factorial(long n)
    {
        if (n == 0)
            return 1;
        return n*factorial(n-1);
    }

    long evenDigit(){
        long dig;
        int s=0;
        while (n!=0) {
            dig = n % 10;
            n /= 10;
            if (dig % 2 == 0) {
                s += factorial(dig);
            }
        }
        System.out.println(s);
        return s;
    }

    public static void main(String[] args){
        question6 ob=new question6();
        ob.input();
        ob.evenDigit();
    }
}
