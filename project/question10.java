import java.util.*;
public class question10 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the first string");
        String s1=sc.nextLine();
        System.out.println("Enter the second string");
        String s2=sc.nextLine();
        String ns="";
        if (s1.length()==s2.length()){
            for(int i=0;i<s1.length();i++){
                ns+=s1.charAt(i);
                ns+=s2.charAt(i);
            }
            System.out.println("Final string: "+ns);
        }
        else{
            System.out.println("Invalid Input");
        }
    }
}
