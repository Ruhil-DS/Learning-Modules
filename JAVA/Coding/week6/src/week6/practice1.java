package week6;

import java.util.*;
public class practice1 {
public static void main(String[] args) {
//Scanner sc = new Scanner(System.in);
//String s = sc.nextLine();
//sc.close();
//// Fill the code here
//TreeMap<Character, Integer> word = new TreeMap<Character, Integer>();
//
//for(int i=0; i<s.length(); i++) {
//	Character c = s.charAt(i);
//	word.putIfAbsent(c,0);
//}
//
//for(int i=0; i<s.length(); i++) {
//	Character c = s.charAt(i);
//	if(word.get(c) == 0) {
//		System.out.print(c);
//		word.put(c, 1);
//	}
//}
	Scanner sc = new Scanner(System.in);
	Integer s = sc.nextInt();	
	sc.close();
	
	onlyPositive(s);
}
public static void onlyPositive(int x) {
	assert x>=0 : x;
	
	System.out.print("The number was = " + x);
}
}