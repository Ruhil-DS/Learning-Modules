import java.util.*;

class FClass{
    private static void caller(Shape s) {
        //check if s is of type Rectangle
    	if(s instanceof Rectangle) {
            System.out.println(s.area());
    	}
        //check if s is of type Cube
    	else if(s instanceof Cube) {
            System.out.println(s.volume());
            }
    }
public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int w = sc.nextInt();
        int h = sc.nextInt();
        int a = sc.nextInt();
        caller(new Rectangle(w, h));
        caller(new Cube(a));
    }
}