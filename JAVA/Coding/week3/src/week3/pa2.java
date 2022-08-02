package week3;

import java.util.*;
class Point{
    private int x, y;
 // implement the constructor and
    Point(int x, int y){
    	this.x = x;
    	this.y = y;
    }
    // override the toString() and equals() methods
    public boolean equals(Point p2){
    	if((this.x == p2.x) && (this.y == p2.y)) {
    		return true;
    	}
    	return false;
    }
    
    public String toString() {
    	return ("("+this.x+", "+this.y+")");
    }
    
}

public class pa2{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x1 = sc.nextInt();
        int y1 = sc.nextInt();
        int x2 = sc.nextInt();
        int y2 = sc.nextInt();
	    
        Point p1 = new Point(x1, y1);
        Point p2 = new Point(x2, y2);
		
        if(p1.equals(p2))
            System.out.println(p1 + "==" + p2);
        else
            System.out.println(p1 + "!=" + p2);
    }
}