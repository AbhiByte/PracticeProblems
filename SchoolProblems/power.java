public class power
{
    public static void main(String[] args)
    {

        System.out.print(exponent(3, 2));
    }

    public static int exponent(int base, int exponent)
    {
        if (exponent == 0)
        {
            return 1;
        }
        else
        {
            return base * exponent(base, exponent - 1);
        }
    }
}
