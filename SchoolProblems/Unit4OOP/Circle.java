public class Circle
{
    double xCooord; //x-coordinate of the centre
    double yCooord; //y-coordinate of the centre
    double radius; //radius

    //Instance methods

    //Area of circle
    public Double areaOfCircle(double radius)
    {
        //A = pi r^2
        return Math.PI * radius * radius;
    }

    public Circle smaller (Circle circle2)
    {
        if (circle2.radius < this.radius)
        {
            return circle2;
        }
        else
        {
            return this;
        }
    }

    public boolean isInside(Circle circle1)
    {
        double radDist = Math.sqrt((circle1.xCooord - this.xCooord)*(circle1.xCooord - this.xCooord) + (circle1.yCooord - this.yCooord)*(circle1.yCooord - this.yCooord));
        if (circle1.radius > (radDist + this.radius))
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    //toString
    public String toString()
    {
        return "Center: (" + xCooord +", "+ yCooord + ") \n Radius: " + radius;
    }

    //Constructors
    public Circle()
    {
        this.xCooord = 0;
        this.yCooord = 0;
        this.radius = 1;
    }

    public Circle(double x, double y, double radius)
    {
        this.xCooord = x;
        this.yCooord = y;
        this.radius = Math.abs(radius);
    }

    public Circle(Circle c1)
    {
        Circle c2 = c1;
    }


}
