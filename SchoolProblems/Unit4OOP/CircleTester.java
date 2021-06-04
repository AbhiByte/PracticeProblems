public class CircleTester
{
    public static void main(String[]args)
    {
        Circle circle1 = new Circle(2, 5, 4);

        Circle circle2 = new Circle(1, 3, 1);

        //Circle circle3 = new Circle(11, -10, 5);


        double distance = Math.pow((circle1.xCooord * circle1.xCooord + circle1.yCooord * circle1.yCooord), 0.5);
        //System.out.println(distance);

        double centreSeparation = Math.pow(Math.pow(circle1.xCooord - circle2.xCooord, 2) + Math.pow(circle1.yCooord -circle2.yCooord , 2), 0.5);
        //System.out.println(centreSeparation);

        double minDistance = centreSeparation - circle1.radius - circle2.radius;
        if (minDistance < 0)
        {
            minDistance = 0;
        }

        //System.out.println(minDistance);


        //Part B d)
        //if (circle1.areaOfCircle(circle1.radius) == circle2.areaOfCircle(circle2.radius))
        //{
            //System.out.println("True");
        //}
        //else
        //{
            //System.out.println("Not true");
        //}

        //System.out.println(equalOrNot(circle1, circle2));

        //System.out.println(circle1.toString());
        //System.out.println(circle2.toString());

        System.out.println(circle2.isInside(circle1));

    }

    //Part B g)
     public static boolean equalOrNot(Circle c1, Circle c2)
    {
        if (c1.radius == c2.radius)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}
