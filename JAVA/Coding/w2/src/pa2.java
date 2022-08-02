import java.util.*;
public class pa2 {
  
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    String s1 = sc.next();
    evenDisplay(s1);
  }
// Define evenDisplay(String) method here
// Write a program to accept a string input from user and print the characters at even indices.
// Microsoft -  Mcoot

  public static void evenDisplay(String s) {
	  
	  int len = s.length();
	  
	  for(int i=1;i<len+1;i+=2)
		  System.out.print(s.substring(i-1, i));
	 
  }
}