import java.util.*;
import java.io.*;
public class question4 {
    int productcode;
    String flavour,packtype;
    int packsize,productprice;
    void input(){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the product code");
        productcode=sc.nextInt();
        System.out.println("Enter the flavour");
        flavour=sc.nextLine();
        System.out.println("Enter the pack type");
        packtype=sc.nextLine();
        System.out.println("Enter the pack size");
        packsize=sc.nextInt();
        System.out.println("Enter the product prize");
        productprice=sc.nextInt();
    }

    void display(){
        System.out.println("product code is: "+productcode);
        System.out.println("product price is: "+productprice);
        System.out.println("flavour is: "+flavour);
        System.out.println("pack size is: "+packsize);
        System.out.println("pack type is: "+packtype);
    }

    void discount(){
        productprice=(int)(productprice-(productprice*0.1));
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        question4 ob=new question4();
        ob.input();
        ob.display();
        ob.discount();
        ob.display();
    }
}
