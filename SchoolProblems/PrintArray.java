public class PrintArray{

	public static void main(String[] args) {

	int[][] yourArray = {{1, 2, 4}, {4, 7, 6}, {5, 7, 8}};
	print(yourArray);

    }
	public static void print(int[][]theArrayYouWantToPrint)
	{
		//System.out.println("Your array is: ");
		for (int i = 0; i < theArrayYouWantToPrint.length; i++)
		{
			for (int j = 0; j < theArrayYouWantToPrint[i].length; j++)
			{
				System.out.print(theArrayYouWantToPrint[i][j]+"\t");
			}
			System.out.println();
		}
	}
}
