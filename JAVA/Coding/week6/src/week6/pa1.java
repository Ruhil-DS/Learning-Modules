package week6;

import java.util.*;
class RemoveStudent{
	    public boolean property(Double value) {
		        if(value<65)
			            return true;
	        return false;				
	    }
	    
	    
		public void detained(Map<String, Double> obj) {
// Define the detained() method}}
	    	String[] arr = new String[6];
	    	int i = 0;
	    	for(Map.Entry<String, Double> e: obj.entrySet()) {
                String K = e.getKey();
                double V = e.getValue();
                if(property(V) == true) {
            		arr[i++] = K;
                }
          }
	    	for(int j=0; j<6;j++) {
	    		if(arr[j] != null) obj.remove(arr[j]);
	    	}
	    	System.out.println(obj);
//	    	for(Map.Entry<String, Double> entry: obj.entrySet()){
//	    		String k = entry.getKey();
//	    		Double v = entry.getValue();
//	    		System.out.println(k + v);
//	    		if(property(v)) {
//	    			obj.remove(k);
//	    		}
//	    	}
	    	
}
	    public void display(Map<String, Double> obj) {
		        System.out.println(obj);
	    }
}
public class pa1 {
	    public static void main(String[] args) {
		        Map<String,Double> map=new TreeMap<String,Double>();
		        Scanner scanner=new Scanner(System.in); 
		        for (int i=0; i<3; i++) {
			            map.put(scanner.next(),scanner.nextDouble());
		        }
		        RemoveStudent obj=new RemoveStudent();
		        obj.detained(map);
	    }
}