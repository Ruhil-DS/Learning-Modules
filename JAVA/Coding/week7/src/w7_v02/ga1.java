package w7_v02;

import java.util.*;
//Define DivisionException class here

class DivisionException extends Exception{
	DivisionException(){
		super("Division by 3 is not allowed");
	}
}

public class ga1{

  //Define divide(int a, int b) here
	public static double divide(int a, int b) throws DivisionException{
		if(b==3) {
			throw new DivisionException();
		}
		else return a/b;
	}

  public static void main(String[] args) {
     Scanner sc = new Scanner(System.in);
     int x = sc.nextInt();
     int y = sc.nextInt();
 
     //call divide method here
    try {
    	var e = divide(x, y);
    	System.out.println(e);
    }
    catch(Exception e){
    	System.out.println(e);
    }
    finally {
    	sc.close();
    }
    }
    		
     
  }
