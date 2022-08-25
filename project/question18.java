public class question18 {
    public static void main(String[] args){
        int sal[]={50000,40000,30000,80000,90000};
        String names[]={"rishabh","rishik","ashutosh","yathin","neeraj"};
        for(int i=0;i<names.length;i++){
            if (sal[i]<50000){
                System.out.println(names[i]);
            }
        }
    }
}
