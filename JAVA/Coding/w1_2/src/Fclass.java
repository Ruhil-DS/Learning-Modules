import java.util.Scanner;

public class Fclass
{
    public static void main(String[] args) 
    {
        Scanner s = new Scanner(System.in);
    	   String project[] = {"P001","P002","P003"};
        //Enter the id of employee
        String id = s.nextLine();
        //Enter the name of employee
        String name = s.nextLine();
        
        Employee e1 = new Employee(id,name,project);
        Employee e2 = new Employee(e1); 
        //The copy constructor must copy all the data members. 
       
        //e1.mutator();
        
        e2.display();
    }
}


/*
id:e005
name:Patrick
projects:
P001:P002:P003:
*/