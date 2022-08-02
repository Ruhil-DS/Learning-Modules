class Cube extends Shape{
    private int a;
    //implement Cube class
    public Cube(int a) {
    	this.a = a;
    }
    public int volume() {
    	return (a*a*a);
    }
}