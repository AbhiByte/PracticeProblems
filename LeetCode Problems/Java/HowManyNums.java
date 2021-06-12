public class HowManyNums
{
    public static void main(String[]args)
    {
        int[] nums = {8,1,2,2,3};
        System.out.println(answer(nums));
    }

    public static int[] answer(int[]nums)
    {
        int[] ans = new int[nums.length];
        for (int i = 0; i < nums.length; i++)
        {
            int tempAns = 0;
            for (int j = 0; j < nums.length; j++)
            {
                if (i != j)
                {
                    tempAns += 1;
                }
            }
            ans[i] = tempAns;
        }
        return ans;
    }
}
