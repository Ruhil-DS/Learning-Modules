package week7;

import java.util.*;

public class pa2{
   
 //implement function replace()



public static char[] replace(char s[], int i, char c) {
	try {
		
		
		 
		s[i] = c;
		return s;

		
	}
	catch (ArrayIndexOutOfBoundsException e){
        if (i >= s.length) {
            s[s.length - 1] = c;
            return s;
        } else {
            throw e;
        }
    }
	
}


	


 public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s1 = sc.next();
        int i = sc.nextInt();
        char c = sc.next().charAt(0);
        try {
            String s2 = new String(replace(s1.toCharArray(), i, c));
            System.out.println(s2);
        } 
        catch(Exception e) {
            System.out.println(e.getMessage());
        }
    }
}


	
	