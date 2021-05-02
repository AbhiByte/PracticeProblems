public class GoodPairs
{
    public static void main(String[]args)
    {
        int[] nums = {1, 2, 3};
        System.out.println(good(nums));
    }

    public static int good(int[]nums)
    {
        int ans = 0;
        for (int i = 0; i < nums.length; i++)
        {
            for (int j = 1; j < nums.length; j++)
            {
                if (i < j && nums[i] == nums[j])
                {
                ans++;
                }
            }
        }
        return ans;
    }
}
