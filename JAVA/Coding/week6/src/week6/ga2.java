package week6;

import java.util.*;

public class ga2{
    public static boolean balanceCheck(String sequence) {
//Write your code here

Stack<Character> balancer = new Stack<Character>();
        
        for(int i=0;i<sequence.length();i++) {
            Character ch = sequence.charAt(i);
            if (ch == '{' || ch == '(' || ch == '[') {
            	balancer.push(ch);
            	continue;
            }
            if(balancer.isEmpty()) {
            	return false;
            }
            Character check;
            switch(ch){
            case '}':
            	check = balancer.pop();
            	if(check == '[' || check == '(') {
            		return false;
            	}
            	break;
            case ']':
            	check = balancer.pop();
            	if(check == '{' || check == '(') {
            		return false;
            	}
            	break;
            case ')':
            	check = balancer.pop();
            	if(check == '[' || check == '{') {
            		return false;
            	}
            	break;
            	
            }
            			
            }
        return (balancer.isEmpty());
        }
            
 
        
   
    public static void main(String args[]) {
        Scanner s = new Scanner(System.in);
        
        ArrayList<String> expr_arr= new ArrayList<String>();
        String inp=null;
        
        do {
            inp = s.nextLine();
            if(!inp.equalsIgnoreCase("Done"))
                expr_arr.add(inp);
        }while(!inp.equalsIgnoreCase("Done"));

        for(String expr : expr_arr) {
            if(balanceCheck(expr)) {
                System.out.println("Balanced");
            }
            else {
                System.out.println("Not Balanced");
            }
        }
    }
}     