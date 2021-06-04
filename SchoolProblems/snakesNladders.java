import java.util.Random;
import java.util.*;
public class snakesNladders
{
    public static void main (String[]args)
    {
        int[][] gameBoard = new int [6][6];

        System.out.println(determineFirst());
        PrintArray.print(intBoard(gameBoard));


        //Test variables
        int[]currPosition = {0, 0};
        int roll = 0;
        //Test call to the method
        allMoves(currPosition, roll, gameBoard);
        //Printing the results
        System.out.print("["+ currPosition[0] + ", " + currPosition[1] + "]");









    }

    public static int determineFirst()
    {
        Random rand = new Random();
        int player = rand.nextInt(6 - 1 + 1) + 1;
        int npc = rand.nextInt(6) + 1;
        if (player < npc)
        {
            player = 1;
            return player;
        }
        else
        {
            npc = 0;
            return npc;
        }

    }

    public static int[][] intBoard (int[][]gameArray)
    {
		for (int i = 0; i < gameArray.length; i++) {

			if (i % 2 == 0)
            {
				int num = gameArray.length * (gameArray.length - i);
				for (int j = 0; j < gameArray[i].length; j++)
                {
					gameArray[i][j] = num;
					num--;
				}
			}//
			else {
				int num = gameArray.length * (gameArray.length - (i + 1))+ 1;
				for (int j = 0; j < gameArray[i].length; j++) {
					gameArray[i][j] = num;
					num++;
				}

			}
		}//for i
        return gameArray;
	}

    public static String[][] strBoard (String[][] textArray)
    {
        textArray[textArray.length - 1][textArray[0].length - 1] = "Start";
        return textArray;
    }

    public static int roller()
    {
        Random random = new Random();
        int roll = random.nextInt(6 - 1 + 1) + 1;
        return roll;

    }
    //This method checks for if the current position is a chute/ladder or a normal square
    //Only this method needs to be called in the main method
    public static int[] allMoves (int[] arrCurrPos, int rollNum, int[][]board)
    {
        //This method needs access to the positions of snakes and ladders so it is given here
        int[][]posOfLaddersAndChutes = {{2, 10}, {18, 30},{23, 27}, {29, 35}, {34, 4}, {22, 14}, {17, 8}, {12, 1}};

        //Interating through each row of the ladders and chutes 2D array
        for (int i = 0; i < posOfLaddersAndChutes.length; i++)
        {   //If the current position is the start of a ladder or chute, then run the ladder method
            if (board[arrCurrPos[0]][arrCurrPos[1]] == posOfLaddersAndChutes[i][0])
            {
                chutesLadders(arrCurrPos, board);
            }
        }
        /*"Else" run the update position method which will make a move and then check to see if the square the player
        lands on is a chute or ladder. If yes, then the ladder method will be called again. */
        regularMove(arrCurrPos, rollNum, board);
        //Checking if end game position has been reached
        if (arrCurrPos[0] == 0 && arrCurrPos[1] == 0)
        {
            System.out.println("Game over, you won!");
        }
        return arrCurrPos;

    }
    /*This method is for a regular move. It works by calculating the final position and then finding the value of the final
    position in the game board and updating the currPos value*/
    public static int[] regularMove (int[] arrCurrPos, int rollNum, int[][]board)
    {   //This method needs to know the location of chutes/ladders since we call the ladder method inside this method
        int[][]posOfLaddersAndChutes = {{2, 10}, {18, 30},{23, 27}, {29, 35}, {34, 4}, {22, 14}, {17, 8}, {12, 1}};
        //Sum, aka the final position which is equal to the currPos + roll num
        int sum = rollNum + board[arrCurrPos[0]][arrCurrPos[1]];
            //If we are not in an end game scenario
            if (sum <= (board.length * board[0].length))//End game checker
            {   //Iterating through the entire board and finding the sum value
                for (int i = 0; i < board.length; i++)
                {
                    for (int j = 0; j < board[i].length; j++)
                    {   //If the sum value is found
                        if (board[i][j] == sum)
                        {   //Update currPos to the i, j values of the board
                            arrCurrPos[0] = i;
                            arrCurrPos[1] = j;
                        }
                    }
                }
            }
        //Then, run ladder method (It automatically checks to see if a ladder/chute move is possible and then runs if possible)
        chutesLadders(arrCurrPos, board);
        //Return new currPos of player
        return arrCurrPos;
    }

    public static int[] chutesLadders (int[] arrCurrPos, int[][]board)
    {
        //Based on research, given and n x n grid, there should be n - 2 chutes and n - 2 ladders
        //In this test case, we are using a 6 x 6 grid so 4 ladders
        //First 4 rows are ladders (start value < end value) and last 4 rows are chutes (start value > end value)
        int[][]posOfLaddersAndChutes = {{2, 10}, {18, 30},{23, 27}, {29, 35}, {34, 4}, {22, 14}, {17, 8}, {12, 1}};
        //For every row in the posOfLaddersAndChutes array...
        for (int i = 0; i < posOfLaddersAndChutes.length; i++)
        {   //if the currPos equals the the first value of the row
            if (board[arrCurrPos[0]][arrCurrPos[1]] == posOfLaddersAndChutes[i][0])
            {   //Iterate through the whole board the find the desired value
                for (int m = 0; m < board.length; m++)
                {
                    for (int n = 0; n < board[m].length; n++)
                    {   //If the board value equals the end value of the chute/ladder
                        if (board[m][n] == posOfLaddersAndChutes[i][1])
                        {   //update currPos to m, n values of the board
                            arrCurrPos[0] = m;
                            arrCurrPos[1] = n;
                        }
                    }
                }
            }
        }
        //Return updated position
        return arrCurrPos;
    }

}
