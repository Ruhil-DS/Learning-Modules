class ContactEmployee extends Employee{
    final private static double hourlyPay = 100.00;
    private int contactHour;
	
    //implement the constructor
    public ContactEmployee(String name, long aadharno, int cont) {
    	super(name, aadharno, cont*hourlyPay);
    }
    
    //salary is computed as contactHour * hourlyPay
    public void print() {
    	
    	super.print();
    }
    
    
}