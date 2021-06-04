public class BottleTester
{
    public static void main (String[] args)
    {
        WaterBottle bottle1 = new WaterBottle();
        bottle1.setCapRadius(5);
        bottle1.setBottleHeight(10);
        bottle1.setBottleRadius(4);
        bottle1.setMaterialType("Plastic");

        WaterBottle bottle2 = new WaterBottle(5, 10, 4, "Plastic");

        System.out.println(bottle1);
        System.out.println("..............................");
        System.out.println(bottle2);

        System.out.println(bottle1.equals(bottle2));


    }
}
