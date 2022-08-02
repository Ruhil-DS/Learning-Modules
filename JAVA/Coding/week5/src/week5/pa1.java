package week5;

import java.lang.reflect.*;
import java.util.*;
class ClassStats{
public static int getPubMethodCount(String cname) {
        try {
            //add code to return the count of 
        	Class o = Class.forName(cname);
        	Method[] methods = ((Class<?>) o).getMethods();
        	return methods.length;
            //public methods in the given class		
        }catch(Exception e) { return -1; }
    }
    public static int getAllMethodCount(String cname) {
        try {
            //add code to return the count of all
        	
        	Class o = Class.forName(cname);
        	Method[] methods = ((Class<?>) o).getDeclaredMethods();
        	return methods.length;
            //declared methods in the given class		
        }catch(Exception e) { return -1; }
    }
    public static int getPubFieldCount(String cname) {
        try {
            //add code to return the count of 
        	
        	Class o = Class.forName(cname);
        	Field[] fields = ((Class<?>) o).getFields();
        	return fields.length;
            //public fields (instance variables) in the given class
        }catch(Exception e) { return -1; }
    }
    public static int getAllFieldCount(String cname) {
        try {
            //add code to return the count of
        	
        	Class o = Class.forName(cname);
        	Field[] fields = ((Class<?>) o).getDeclaredFields();
        	return fields.length;
            //all fields (instance variables) in the given class
        }catch(Exception e) { return -1; }
    }
    public static int getPubContCount(String cname) {
        try {
            //add code to return the count of 
        	
        	Class o = Class.forName(cname);
        	Constructor[] consts = ((Class<?>) o).getConstructors();
        	return consts.length;
            //public constructors in the given class
        }catch(Exception e) { return -1; }		
    }
    public static int getAllContCount(String cname) {
        try {
            //add code to return the count of
        	
        	Class o = Class.forName(cname);
        	Constructor<?>[] consts = ((Class<?>) o).getDeclaredConstructors();
        	return consts.length;
            //all constructors in the given class
        }catch(Exception e) { return -1; }
    }
}

public class pa1{
    public static void main(String[] args) {
        String cname;
        Scanner sc = new Scanner(System.in);
        cname = sc.nextLine();
        System.out.println("Constructor: " + 
                        ClassStats.getPubContCount(cname) + ", " + 
                        ClassStats.getAllContCount(cname));
        System.out.println("Fields: " + 
                        ClassStats.getPubFieldCount(cname) + ", " +
                        ClassStats.getAllFieldCount(cname));
        System.out.println("Methods: " + 
                        ClassStats.getPubMethodCount(cname) + ", " +
                        ClassStats.getAllMethodCount(cname));
    }
}