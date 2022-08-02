package week7;

import java.util.*;

//Define class WrongDestinationException
class WrongDestinationException extends Exception{
	
	public String toString(){
		return "WrongDestinationException: Invalid destination";
	}
	public Throwable getCause() {
		Exception newe = new WrongDestinationException();
		newe.initCause(new NullPointerException());
		return newe;
	}
}

//Define class ImproperHeadCountException
class ImproperHeadCountException extends Exception{
	
	public String toString() {
		return "ImproperHeadCountException: Head count should be positive non-zero value";
	}
	
	public Throwable getCause() {
		Exception newe = new ImproperHeadCountException();
		newe.initCause(new ImproperHeadCountException());
		return newe;
	}
}

class CarRental{
  int passenger_count;
  String chosen_destination;
  HashMap<String,Double> available_destinations;  
	
  public CarRental(int pc, String dest) {
      passenger_count = pc;
      chosen_destination = dest;
      //preassigned destinations and total car fare
      //Leave the code below as it is
      available_destinations = new HashMap<String,Double>();
      available_destinations.put("Marina Beach", 2000.0);
      available_destinations.put("Elliot's Beach", 5000.0);
      available_destinations.put("Film City", 8000.0);
  }
  public void carBooker() throws ImproperHeadCountException, WrongDestinationException{
      //define this method according to the problem description
	  
	  try {
	  if(this.passenger_count <=0) {
		  throw new ImproperHeadCountException();
	  }
	  else if(this.available_destinations.getOrDefault(chosen_destination, null) == null) {
		 throw new WrongDestinationException(); 
	  }
	  else {
		  System.out.println("Destination: "+ this.chosen_destination + ", Head cost: "+ 
				  (this.available_destinations.get(chosen_destination)/this.passenger_count) );
	  }
	  
	  }
	  catch(ImproperHeadCountException e){
		  System.out.println(e);
	  }
	  catch(WrongDestinationException e){
		  System.out.println(e);
	  }
  }

}
public class pa1{
  public static void main(String args[]) {
      Scanner s = new Scanner(System.in);
      
      int num = s.nextInt(); //input the number of car rental requests
      try {
          for(int i=1;i<=num;i++) {
              int heads = s.nextInt(); //enter head count
              s.nextLine();  //enter destination
              String dest = s.nextLine();     
              CarRental obj = new CarRental(heads,dest);
              obj.carBooker();
          }
      }catch(Exception e) {
          System.out.println(e.getCause());
      }
      finally {s.close();}
  }
}