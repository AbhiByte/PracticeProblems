public class RunningSum
{
    public static void main(String[]args)
    {
        int[] myList = {1, 1, 1, 1, 1};
        int[] ans = running(myList);
        for (int x = 0; x < ans.length; x++)
        {
            System.out.println(ans[x]);
        }

    }

    public static int[] running(int[] arr)
    {
        int length = arr.length;
        int[]finalArr = new int [length];
        finalArr[0] = arr[0];
        int counter = 0;
        int sum = 0;

        for (int i = 1; i < arr.length; i++)
        {
            counter = i;
            while (counter >= 0)
            {
                sum += arr[counter];
                counter--;
            }
            counter = 0;
            finalArr[i] = sum;
            sum = 0;
        }

        return finalArr;
    }
}
