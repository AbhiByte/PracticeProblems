public class poop
{
    public static void main(String[]args)
    {
        int[][] account = {{1, 2, 3}, {3, 2, 1}};
        System.out.println(rich(account));
    }
    public static int rich (int[][]accounts)
    {
        int sum = 0;
        int ans = 0;
        int i = 0;

        for (int x : accounts[i])
        {
            sum += x;
            if (sum > ans)
            {
                ans = sum;
            }
        }
        return ans;
    }
}
