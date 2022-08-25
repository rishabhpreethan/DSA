public class question9 {
    float a,b,c,d;
    double r1,r2;
    void quad(float x,float y,float z){
        a=x;
        b=y;
        c=z;
        d=0;
    }

    void calculate(){
        d=(b*b)-4*a*c;
        if(d<0){
            System.out.println("Roots not possible");
        }
        else{
            r1=(-b+Math.sqrt(d))/2*a;
            r2=(-b-Math.sqrt(d))/2*a;
            System.out.println("The roots are: "+r1+r2);
        }
    }

    public static void main(String[] args){
        question9 ob=new question9();
        ob.quad(4.0f,5.0f,8.0f);
        ob.calculate();
    }
}
