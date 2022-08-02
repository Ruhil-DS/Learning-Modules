class Rectangle extends Shape{
    private int w, h;
//implement Rectangle class
    public Rectangle(int w, int h) {
    	this.w = w;
    	this.h = h;
    }
    public int area() {
    	return (this.w * this.h);
    }
}