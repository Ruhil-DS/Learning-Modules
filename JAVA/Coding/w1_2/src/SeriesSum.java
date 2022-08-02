import java.util.*;
public class SeriesSum {
	
	public static int square(int x) {
		return x*x;
	}
	
	public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int sum = 0;
    for(int i=1; i<=n; i++) {
    	for(int j=0; j<=i; j++) {
    		sum += square(j);
    	}
    }

    System.out.println(sum);
    
  }
}