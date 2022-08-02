package week6;

import java.util.*;

abstract class Account implements Comparable<Account>{
    String acc_no;
    double balance;	
    public Account(String no,double bal){
        acc_no = no; 
        balance = bal;
    }	
//Override "compareTo" method here
    public int compareTo(Account act) {
    	if(this.balance > act.balance) return -1;
    	else if(this.balance < act.balance) return 1;
    	else return 0;
    }

// Override "equals" method here
    public boolean equals(Object o) {
    	if (this==o) return true;
    	
    	if (o instanceof Account) {
    		
            return this.acc_no.equals(((Account)o).acc_no);
    	}
    	return false;
    }

// Override "hashCode" method here
    public int hashCode(){
        return this.acc_no.hashCode();
    }
}
class SavingsAccount extends Account{
    public SavingsAccount(String acc_no, double bal) {
        // Complete the definition
    	super(acc_no, bal);
    }
    // Override the toString() method
    public String toString() {
    	return ("Savings Account:" + this.acc_no + ", Balance:" + this.balance);
    }

}

    


class CurrentAccount extends Account{
    double overdraft_limit;
    public CurrentAccount(String acc_no, double bal, double odl) {
        // Complete the constructor definition}}
    	super(acc_no, bal);
    	this.overdraft_limit = odl;
    }

    // Override the toString() method}}
    public String toString() {
    	return ("Current Account:" + this.acc_no + ", Balance:" + this.balance);
    }
}

public class pa2 {
     // Define the `accountProcessor' method here
	public static void accountProcessor(ArrayList<Account> acc) {
		Set<Account> accSet = new LinkedHashSet<>(acc);
        accSet = new TreeSet<>(accSet);
        for (Account a: accSet)
            System.out.println(a);
	}
	

 public static void main(String args[]) {
        Scanner s = new Scanner(System.in);
        ArrayList<Account> acc = new ArrayList<Account>();
        
        //reading the number of savings accounts
        int s_acc_count = s.nextInt();
        for(int i=1;i<=s_acc_count;i++) {
            //reading acc no
            String no = s.next();
            //reading balance
            double bal = s.nextDouble();
            acc.add(new SavingsAccount(no,bal));
        }
        
        //reading the number of current accounts
        int c_acc_count = s.nextInt();
        for(int i=1;i<=c_acc_count;i++) {
            //reading acc no
            String no = s.next();
            //reading balance
            double bal = s.nextDouble();
            //reading overdraft limit
            double lim = s.nextDouble();
            acc.add(new CurrentAccount(no,bal,lim));
        }
        
        accountProcessor(acc);
        }
}



/*
3
111 2000
222 1000
111 5000
2
444 1200 50000
111 6000 50000



import java.util.*;

abstract class Account implements Comparable<Account>{
    String acc_no;
    double balance;	
    public Account(String no,double bal){
        acc_no = no; 
        balance = bal;
    }	
//Override "compareTo" method here
    public int compareTo(Account acc){
        return Double.compare(acc.balance, this.balance);
    }
// Override "equals" method here
    public boolean equals(Object ob){
        if (this==ob)
            return true;
        if (ob instanceof Account){
            Account a = (Account)ob;
            return this.acc_no.equals(a.acc_no);
        }
        return false;
    }
// Override "hashCode" method here
    public int hashCode(){
        return this.acc_no.hashCode();
    }
}
class SavingsAccount extends Account{
    public SavingsAccount(String acc_no, double bal) {
        // Complete the definition
        super(acc_no, bal);
    }
    // Override the toString() method
    public String toString(){
        return ("Savings Account:"+this.acc_no+" , Balance:"+this.balance);
    }
}
class CurrentAccount extends Account{
    double overdraft_limit;
    public CurrentAccount(String acc_no, double bal, double odl) {
        // Complete the constructor definition
        super(acc_no, bal);
        this.overdraft_limit = odl;
    }
    // Override the toString() method
    public String toString(){
        return ("Current Account:"+this.acc_no+" , Balance:"+this.balance);
    }
}
public class pa2 {
     // Define the `accountProcessor' method here
    public static void accountProcessor(ArrayList<Account> acc){
        Set<Account> accSet = new LinkedHashSet<>(acc);
        accSet = new TreeSet<>(accSet);
        for (Account a: accSet)
            System.out.println(a);
    }
   public static void main(String args[]) {
          Scanner s = new Scanner(System.in);
          ArrayList<Account> acc = new ArrayList<Account>();
          
          //reading the number of savings accounts
          int s_acc_count = s.nextInt();
          for(int i=1;i<=s_acc_count;i++) {
              //reading acc no
              String no = s.next();
              //reading balance
              double bal = s.nextDouble();
              acc.add(new SavingsAccount(no,bal));
          }
          
          //reading the number of current accounts
          int c_acc_count = s.nextInt();
          for(int i=1;i<=c_acc_count;i++) {
              //reading acc no
              String no = s.next();
              //reading balance
              double bal = s.nextDouble();
              //reading overdraft limit
              double lim = s.nextDouble();
              acc.add(new CurrentAccount(no,bal,lim));
          }
          
          accountProcessor(acc);
          }
}
*/