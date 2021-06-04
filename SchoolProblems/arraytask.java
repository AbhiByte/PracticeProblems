public class arraytask
{
    public static void main(String[]args)
    {
        int[][]ourArray = new int[4][8];
        PrintArray.print(fillArray(ourArray));
    }
public static int[][] fillArray(int[][]array)
{

    for (int i = 0; i < array.length; i++)
    {
        for (int j = 0; j < array[i].length; j++)
        {
            array[i][j] = (2*j + 1) + 16*i;
        }
    }
    return array;
}
}
