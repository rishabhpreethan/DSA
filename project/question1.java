import java.util.*;
public class question1 {
    public static void main(String[] args){
        int m=0;
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter your choice");
        int ch=sc.nextInt();
        switch(ch){
            case 1:
                for(int i=1;i<=4;i++){
                    for(int j=1;j<=i;j++){
                        System.out.print(++m);
                    }
                    System.out.println();
                }
                break;

            case 2:
                char c='A';
                for(int i=5;i>=0;i--){
                    for(int j=0;j<i;j++){
                        System.out.print(c);
                    }
                    c+=2;
                    System.out.println();
                }

        }
    }
}
