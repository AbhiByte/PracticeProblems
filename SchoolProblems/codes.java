public class codes
{
    public static void main(String[]args)
    {
        int[][]array = new int[4][8];
        PrintArray.print(fillArray(array));
    }

    //This method fills an array just like cardA in the question given.
    //It works by interating through each index using for loops and applying a rule (given below) to each index based on the row and col numbers of the index.
    public static int[][]fillArray(int[][]cardA)//input a blank array of size [4][8].
    {
        //For each row in the array
        for (int i = 0; i < cardA.length; i++)
        {
            //For each column in the 2D array
            for (int j = 0; j < cardA[i].length; j++)
            {
                //If the column index value is a multiple of 2
                if(j % 2 == 0)
                {   //This pattern successfully fills even numbered column indices
                    cardA[i][j] = 2*(i + j) + 2 + 14*i;
                }
                //Else, meaning if column index value is odd
                else
                {   //This pattern fills the odd numbered column indices
                    cardA[i][j] = 2*(i + j)+1+14*i;
                }
            }
        }
        //Returning the final 2D array
        return cardA;
    }

}
