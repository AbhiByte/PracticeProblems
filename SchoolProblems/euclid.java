public class euclid
{
    public static void main(String[]args)
    {

        System.out.println(algorithm(18, 24));

    }//main

    public static int algorithm(int m, int n)
    {
        if (m == 0)
        {
            return n;
        }
        if (n == 0)
        {
            return m;
        }
        if (m == n && m != 0 && n != 0)
        {
            return m;
        }
        if (m > n&& m != 0 && n != 0)
        {
             return algorithm(n, m-n);
        }
        if (m < n && m != 0 && n != 0)
        {
             return algorithm(n, m);
        }
        return m;
    }

}
