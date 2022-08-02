package week5;

import java.util.*;
class ConvertArrays{
	    public Double doubleArr[]=new Double[3];
	    public Integer intArr[]=new Integer[3];
	    public int x=0,y=0,z=0;
	    public void convert(String[] arr){
//loop through the arr and store each element
	    	for(String el: arr) {
	    		if(el.contains(".")) {
	    			doubleArr[x] = Double.parseDouble(el);
	    			x++;
	    		}
	    		else {
	    			intArr[y] = Integer.parseInt(el);
	    			y +=1;
	    		}
	    	}
//in the appropriate array
}
	    public <T> void display(T[] arr){
	        for(T elements:arr)
	    	        System.out.print(elements+" ");
	        System.out.println();
	    }
}
public class pa2 {
	    public static void main(String[] args) {
		    Scanner scanner=new Scanner(System.in);
		    String arr[]= new String[6];
		    for (int i = 0; i < arr.length; i++) {
			        arr[i]=scanner.next();
		    }
	    ConvertArrays conArrays=new ConvertArrays();
	    conArrays.convert(arr);
	    System.out.println("===After conversion Arrays===");
	    conArrays.display(conArrays.doubleArr);
	    conArrays.display(conArrays.intArr);	    
	}
}