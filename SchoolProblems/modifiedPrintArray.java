import java.util.*;
import java.util.Random;
public class modifiedPrintArray{

	public static void main(String[] args) {

	Random random = new Random();
	int[][] yourArray = new int [5][7];
	for (int i = 0; i < yourArray.length; i++)
	{
		for (int j = 0; j < yourArray[i].length; j++)
		{
			yourArray[i][j] = random.nextInt(500 - 100 + 1) + 100;
		}
	}
	yourArray[0][0] = 0;
	yourArray[4][4] = 0;
	yourArray[4][5] = 0;
	yourArray[4][6] = 0;


	print(yourArray);

    }
	public static void print(int[][]theArrayYouWantToPrint)
	{
		for (int i = 0; i < theArrayYouWantToPrint.length; i++)
		{
			for (int j = 0; j < theArrayYouWantToPrint[i].length; j++)
			{
				if (theArrayYouWantToPrint[i][j]!=0)
				{
            		System.out.print(theArrayYouWantToPrint[i][j] + "\t");
				}
				else
				{
					System.out.print("\t");
				}
			}
			System.out.println();
		}
	}
}
