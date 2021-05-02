
public class greatestCandy
{
    public static void main(String[]args)
    {
        int[] my = {12, 1, 12};


        boolean[] hi = candies(my, 10);
        for (int x = 0; x < hi.length; x++)
        {
            System.out.println(hi[x]);
        }

    }

    public static boolean[] candies(int[]candy, int extra)
    {
        int length = candy.length;
        boolean[]boolCandy = new boolean [length];
        int maxVal = 0;
        for (int j = 0; j < candy.length; j++)
        {
            if (candy[j] > maxVal)
            {
                maxVal = candy[j];
            }
        }

        for (int i = 0; i < candy.length; i++)
        {
            if ((candy[i] + extra) >= maxVal)
            {
                boolCandy[i] = true;
            }
            else
            {
                boolCandy[i] = false;
            }
        }
        return boolCandy;
    }

}
