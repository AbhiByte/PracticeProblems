public class mirrorImage
{
    public static void main (String[]args)
    {
        int[][]arr1 = new int[4][7];
        //PrintArray.print(mirrorArr(arr1));

        int[][]arr2 = new int[4][8];
        PrintArray.print(sumGame(arr2));
        PrintArray.print(sumGame2(arr2));

    }
    //Takes a blank 2D array as input and outputs an array as specified in the "Two D Task2" slideshow
    public static int[][] mirrorArr(int[][] arr)
    {

        for (int i = 0; i < arr.length; i++)
        {
            //Filling in the first three columns
            for (int j = 0; j < arr[i].length - 4; j++)
            {
                arr[i][j] = (2*j + 1) + 16*i;
            }
            //Filling in the middle column with value '6'
            arr[i][arr.length / 2 + 1] = 6;
            //Filling in the last three columns with the same values as the first three columns
            for (int j = arr[i].length-1; j > arr[i].length / 2 ; j--)
            {
                arr[i][j] = (2*j - 7) + 16*i;
            }
            //Flipping the last three column values to produce mirror image
            for (int j = arr[i].length / 2 + 1; j < arr[i].length; j++)
            {
                arr[i][j] = arr[i][arr[i].length - 1 - j];
            }
        }

        return arr;
    }
    public static int[][] sumGame(int[][]arr)
    {
        for (int i = 0; i < arr.length; i++)
        {
            for (int j = 0; j < 2; j++)
            {
                arr[i][j] = (j + 7) + 16*i;
            }
            for (int j = 2; j < 4; j++)
            {
                arr[i][j] = (j + 9) + 16*i;
            }
            for (int j = 4; j < 6; j++)
            {
                arr[i][j] = (j + 11) + 16*i;
            }
            for (int j = 6; j < 8; j++)
            {
                arr[i][j] = (j + 13) + 16*i;
            }
        }
        return arr;
    }
    //Takes a blank 2D array as input and outputs an array as specified in the second problem of the "Two D Task2" slideshow
    public static int[][] sumGame2(int[][]arr)
    {
        //Going through every index in the array
        for (int i = 0; i < arr.length; i++)
        {

            for (int j = 0; j < arr[i].length; j++)
            {
                //Filling in the first 2 columns
                if (j < 2)
                {
                    arr[i][j] = (j + 7) + 16*i;
                }
                //Filling in the 3rd and 4th columns
                if (j < 4 && j > 1)
                {
                    arr[i][j] = (j + 9) + 16*i;
                }
                //Filling in the 5th and 6th columns
                if (j < 6 && j > 3)
                {
                    arr[i][j] = (j + 11) + 16*i;
                }
                //Filling in the 7th and 8th columns
                if (j < 8 && j > 5)
                {
                    arr[i][j] = (j + 13) + 16*i;
                }
            }
        }
        return arr;
    }



}
