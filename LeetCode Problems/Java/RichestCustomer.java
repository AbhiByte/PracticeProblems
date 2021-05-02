public class RichestCustomer
{
    public static void main(String[]args)
    {
        int[][] accounts = {{2,8,7},{7,1,3},{1,9,5}};
        //System.out.println(accounts[0][1]);
        System.out.println(richest(accounts));
    }
    public static int richest (int[][]accounts)
    {
        int sum = 0;
        int ans = 0;
        for (int i = 0; i < accounts.length; i++)
        {
            for (int j = 0; j < accounts[i].length; j++)
            {
                sum += accounts[i][j];
            }
            if (sum > ans)
            {
                ans = sum;
            }
            sum = 0;


        }

        return ans;
    }
}
