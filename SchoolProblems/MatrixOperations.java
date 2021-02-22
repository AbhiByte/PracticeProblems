
public class MatrixOperations {

	public static void main(String[] args) {
        int[][]matrix1 = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
		int[][]matrix2 =  {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};

		PrintArray.print(matrix1);
		PrintArray.print(matrix2);
		PrintArray.print(productMatrix(matrix1, matrix2));
	}
//Method to calculate product of two matrices
public static int[][] productMatrix(int[][]matrixA, int[][]matrixB)
	{
	//Gets length of row/col for matrix1/2
	int row1 = matrixA.length;

	int col1= matrixA[0].length;

	int row2 = matrixB.length;

	int col2 = matrixB[0].length;
	
	//Output matrix 
	int[][] finalProduct = new int [row1][col2];

	//Compatibility test
	if (row2 != col1)
	{
		System.out.println("Matrices not compatible");
	}

		for (int i = 0; i < row1; i++)
		{
			for (int j = 0; j < col2; j++)
			{
				for (int k = 0; k < row2; k++)
				{
					finalProduct[i][j] += matrixA[i][k] * matrixB[k][j];

				}

			}
		}
		return finalProduct;
	}
}
