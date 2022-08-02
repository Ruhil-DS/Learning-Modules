package week6;

import java.util.*;
class CricketPlayer{
  private String name;
  private int wickets;
  private int runs;
  private int matches;
  public CricketPlayer(String s, int w, int r, int m){
    this.name = s;
    this.wickets = w;
    this.runs = r;
    this.matches = m;
  }
  public String getName(){
    return name;
  }
  public int getWickets(){
    return wickets;
  }
  public int getRuns(){
    return runs;
  }
  public double avgRuns(){
    return runs/matches;
  }
  public double avgWickets(){
    return wickets/matches;
  }
} 
public class ga1 {
public static void displayPlayers(ArrayList<CricketPlayer> BW, ArrayList<CricketPlayer> BT){
//	Print the list of bowlers in a line, followed by the list of batsmen in the next line, 
//	using the displayPlayers(ArrayList<CricketPlayer> bw, ArrayList<CricketPlayer> bt) method.
	for(CricketPlayer c : BW) {
		System.out.print(c.getName() + " ");
	}
	System.out.println();
	for(CricketPlayer c : BT) {
		System.out.print(c.getName() + " ");
	}

}
    

 public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    CricketPlayer p1 = new CricketPlayer(sc.next(), sc.nextInt(), 
                                sc.nextInt(), sc.nextInt());
    CricketPlayer p2 = new CricketPlayer(sc.next(), sc.nextInt(), 
                                sc.nextInt(), sc.nextInt());
    CricketPlayer p3 = new CricketPlayer(sc.next(), sc.nextInt(), 
                                sc.nextInt(), sc.nextInt());
    CricketPlayer p4 = new CricketPlayer(sc.next(), sc.nextInt(), 
                                sc.nextInt(), sc.nextInt());

    // Define ArrayList objects here
    ArrayList<CricketPlayer> temp = new ArrayList<CricketPlayer>();
    ArrayList<CricketPlayer> bw = new ArrayList<CricketPlayer>();
    ArrayList<CricketPlayer> bt = new ArrayList<CricketPlayer>();
    
    temp.add(p1); temp.add(p2); temp.add(p3); temp.add(p4);
    
    for(CricketPlayer c : temp) {
    	// A player is termed as a batsman if his/her average runs per match are greater than 25.
    	// A player is termed as a bowler if his/her average wickets per match are greater than 1.
    	if (c.avgRuns()>25) {
    		bt.add(c);
    	}
    	if (c.avgWickets() > 1) {
    		bw.add(c);
    	}
    }

 displayPlayers(bw, bt);

 }
}

/*
Dhoni
11
11000
347
Kohli
10
12285
257
Ashwin
181
1000
90
Bumrah
130 
50
60
*/