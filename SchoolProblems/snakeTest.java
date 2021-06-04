public class snakeTest
{
    public static void main (String[]args)
    {
        //Variables
        int[][]gameBoard = {{36,35,	34,	33,	32,	31}, {25, 26, 27, 28, 29, 30}, {24,	23,	22	21,	20,	19}, {13,14,	15,	16,	17,	18}, {12, 11,10,9,8,7}, {1,	2,	3,	4,	5,	6}};
        int[]currPosition = {5, 1};
        int roll = 2;

        //Method calling
        updatePostion(currPosition, roll, gameBoard);
        System.out.print("["+ currPosition[0] + ", " + currPosition[1] + "]");
    }
    public static int[] updatePostion (int[] arrCurrPos, int rollNum, int[][]board)
    {
        int[][]posOfLaddersAndSnakes = {{2, 10}, {18, 30},{23, 27}, {29, 35}, {34, 4}, {22, 14}, {17, 8}, {12, 1}};
        int sum = rollNum + board[arrCurrPos[0]][arrCurrPos[1]];

        for (int k = 0; k < posOfLaddersAndSnakes.length; k++)
        {
            if (board[arrCurrPos[0]][arrCurrPos[1]] != posOfLaddersAndSnakes[k][0])
            {
                if (sum <= (board.length * board[0].length))//End game checker
                {
                    for (int i = 0; i < board.length; i++)
                    {
                        for (int j = 0; j < board[i].length; j++)
                        {
                            if (board[i][j] == sum)
                            {
                                arrCurrPos[0] = i;
                                arrCurrPos[1] = j;
                                break;
                            }
                        }
                    }
                }
            }
        }

        ladder(arrCurrPos, board);

        return arrCurrPos;
    }
    public static int[] ladder (int[] arrCurrPos, int[][]board)
    {
        //Based on research, given and n x n grid, there should be n - 2 chutes and n - 2 ladders
        //In this test case, we are using a 6 x 6 grid so 4 ladders
        int[][]posOfLaddersAndSnakes = {{2, 10}, {18, 30},{23, 27}, {29, 35}, {34, 4}, {22, 14}, {17, 8}, {12, 1}};
        for (int i = 0; i < posOfLaddersAndSnakes.length; i++)
        {
            if (board[arrCurrPos[0]][arrCurrPos[1]] == posOfLaddersAndSnakes[i][0])
            {
                for (int m = 0; m < board.length; m++)
                {
                    for (int n = 0; n < board[m].length; n++)
                    {
                        if (board[m][n] == posOfLaddersAndSnakes[i][1])
                        {
                            arrCurrPos[0] = m;
                            arrCurrPos[1] = n;
                        }
                    }
                }
            }
        }

        return arrCurrPos;
    }


}
