public class question8 {

    void num_cal(int num,char ch){
        if (ch=='s' || ch=='S'){
            num=num*num;
            System.out.println(num);
        }
        else {
            num = num * num * num;
            System.out.println(num);
        }
    }

    void num_cal(int a,int b,char ch){
        if (ch=='p' || ch=='P'){
            System.out.println(a*b);
        }
        else {
            System.out.println(a+b);
        }
    }

    void num_cal(String s1,String s2){
        System.out.println(s1==s2);
    }

    public static void main(String[] args){
        question8 ob=new question8();
        ob.num_cal("hello","hello");
        ob.num_cal(4,3,'P');
        ob.num_cal(5,'r');
    }
}
