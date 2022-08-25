public class question7 {

    int volume(int side){
        return side*side*side;
    }

    double volume(double l,double b,double h){
        return l*b*h;
    }

    double volume(double r,double h){
        return Math.PI*r*r*h;
    }

    public static void main(String[] args){
        question7 ob=new question7();
        System.out.println(ob.volume(3));
        System.out.println(ob.volume(3.0,4.0,5.0));
        System.out.println(ob.volume(4.0,6.0));
    }
}
