class Employee extends Person{
    private double salary;

    //implement the constructor
    public Employee(String name, long aadharno, double sal){
    	super(name, aadharno);
    	this.salary = sal;
    }


    //override print method 
    public void print() {
    	super.print();
    	System.out.println("salary : " + this.salary);
    }
}