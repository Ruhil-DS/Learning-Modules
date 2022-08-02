package week4;

import java.util.*;

abstract class StringOperations{
  public abstract String reverse(String s);
  public abstract int vowelCount(String s);
}


/*
 
 Create StringReverse class that extends StringOperations class but defines only String reverse(String s) method. 
 It reverses the string which is passed as parameter and returns the reversed string.
 
Create UpdatedStrings class that extends StringReverse class and defines int vowelCount(String s) method.  
It counts the vowels in the string which is passed as parameter and returns the count.
 */

//Fill the code here
class StringReverse extends StringOperations {
	
	public String reverse(String s) {
	String rev = "";
	int len = s.length();
	
	for(int i=len-1; i>-1; i--) {
		rev+=s.charAt(i);
	}
	return rev;
	}
	
	  public int vowelCount(String s) {
		  return 0;
	  }

   
}

class UpdatedStrings extends StringReverse {
   public int vowelCount(String s) {
	   int count = 0;
	   for(int i = 0; i<s.length(); i++) {
		   if(s.charAt(i) == 'a' || s.charAt(i) == 'e' || 
				   s.charAt(i) == 'i' ||  s.charAt(i) == 'o' || 
				   s.charAt(i) == 'u' ) 
			   count++;
		   
	   }
	   return count;
   }
   
}


class ga1 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String s = sc.next();
    UpdatedStrings str = new UpdatedStrings();
    System.out.println("Reverse of "+ s + " is "+ str.reverse(s));
    System.out.println("Vowel count of "+ s + " is "+ str.vowelCount(s));
  }
}