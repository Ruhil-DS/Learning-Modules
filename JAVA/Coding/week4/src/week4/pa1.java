package week4;

import java.util.*;


interface Searchable{
    public int search(int start_index, Object key);
}
class Char{
    private char c;
    public Char(char c_) {
        this.c = c_;
    }
    public boolean equals(Object d) {
//implement equals() for Char
    	if(d instanceof Char) {
    		if( this.c == ((Char) d).c ){
    			return true;
    		}
    		return false;
    	}
    	return false;
    }
}


class CharArray implements Searchable{
    private Char[] carr;
    public CharArray(Char[] carr_){
        carr = carr_;
    }
    public int search(int start_index, Object key) {
        //search the key in array carr from the index start_index
    	for(int i = start_index; i<carr.length; i++) {
    		if ( carr[i].equals(key)) return i;
    	}
    	return -1;
        //if the key found, return index of the first occurrence of the key
        //else return -1
    }
    public int length() {
    	return carr.length;
    }
}

class FrequencyCounter{
    public static int getFrequency(Searchable ob, Object key){
        if (ob instanceof CharArray) {
            //count occurrences of the key in ob using search function
        	int freq = 0;
        	int ind = 0;
        	while(ind < ((CharArray)ob).length()) {
        		ind = ob.search(ind, key) + 1;
        		if(ind == 0) break;
        		if(ind != -1) freq +=1;
    			//System.out.println("index = " + ind);
        		
        	}
        	return freq;
        	
        	}
        
        else
            return 0;
    }
}
public class pa1{
    public static void main(String[] args) {
        String str;
        char c;
        Scanner sc = new Scanner(System.in);
        str = sc.nextLine();
        c = sc.next().charAt(0);
        Char key = new Char(c);
        Char[] cA = new Char[str.length()]; 
        for(int i = 0; i < str.length(); i++) {
            cA[i] = new Char(str.charAt(i));
        }
        CharArray caObj = new CharArray(cA);
        System.out.println(FrequencyCounter.getFrequency(caObj, key));
    }
}