package week8;

import java.util.*;
import java.util.stream.*;
//define class Employee
class Employee{
	String name;
	String dept;
	int sal;
	Employee(String n, String d, int s){
		this.name = n;
		this.dept = d;
		this.sal = s;
	}
	
	public String toString() {
        return name + " : " + dept + " : " + sal;
    }
	
}

    


class FClass{
	//define method query
	public static Stream<Employee> query(
			ArrayList<Employee> arr, String d, double sal){
		var st = arr.stream()
				.filter(n -> (n.dept.equals(d)
						&& n.sal>=sal));
			return st;
		
		
	}
		
	
	
public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    var eList = new ArrayList<Employee>();
    eList.add(new Employee("Jack", "HR", 30000));
    eList.add(new Employee("Aria", "HR", 40000));
    eList.add(new Employee("Nora", "IT", 50000));
    eList.add(new Employee("Bella", "IT", 60000));
    eList.add(new Employee("Jacob", "IT", 70000));
    eList.add(new Employee("James", "HR", 80000));
    System.out.println("Enter dept : ");
    String d = sc.next();       //read department
    System.out.println("Enter sal : ");
    double s = sc.nextInt();    //read salary
	
    var st = query(eList, d, s);
    st.forEach(n -> System.out.println(n + " "));
}
}
