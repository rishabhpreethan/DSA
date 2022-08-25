import java.util.*;
public class question17 {
    public static void main(String[] args){
        boolean flag=false;
        int r=0;
        String names[]={"rishik","rishabh","raagav","ankith","atharv","rohan","rahul","ashutosh","neeraj","yathin"};
        int phno[]={123,234,345,456,567,678,789,890,134,634};
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the name");
        String n=sc.nextLine();
        for(int i=0;i<names.length;i++){
            if (names[i].equals(n)){
                flag=true;
                r=i;
                break;
            }
            else{
                flag=false;
            }
        }
        if(flag==true){
            System.out.println("Search successful");
            System.out.println("Name: "+names[r]);
            System.out.println("Phno: "+phno[r]);
        }
        else{
            System.out.println("Search Unsuccessful");
        }
    }
}
