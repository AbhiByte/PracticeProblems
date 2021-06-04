import java.util.Random;
public class algorithms
{
    public static void main(String[]args)
    {


        /*long start = System.currentTimeMillis();
		bubbleSort(medArray);
		long end = System.currentTimeMillis( );
		long diff = end - start;
		System.out.println("Time taken: " + diff);
        */
        int[] lister = {4, 3, 1, 6, 5, 9, 8, 2, 7, 10};
        insertionSortInt(lister);
        bubbleSortInt(lister);
        selectionSort(lister);

    }

    public static void insertionSortInt(int [] oneD) {
        int item;
        int toPlace;
        for (int index = 1 ; index < oneD.length; index++) {
            item = oneD[index];
            toPlace = index;
            while (toPlace > 0 && item < oneD[toPlace - 1]) {
                oneD [toPlace] = oneD [toPlace - 1];
                toPlace--;
            }
            oneD[toPlace] = item;
        }//for index
        printInt(oneD);
}
    public static void bubbleSortInt(int [] oneD) {
        int temp;
        for (int index1 = 0; index1<oneD.length;index1++){
            for(int index2 = 1;index2<oneD.length; index2++){
                if(oneD[index2]<oneD[index2-1]){
                    temp = oneD[index2-1];
                    oneD[index2-1] = oneD[index2];
                    oneD[index2] = temp;
                }//if
            }//for index2
            if (index1 == 5){
                printInt(oneD); //Fifth pass
            }
        }//for index1
    }

    public static void selectionSort(int [] arr){
        int n = arr.length;
        // One by one move boundary of unsorted subarray
        for (int i = 0; i < n-1; i++) {
            // Find the minimum element in unsorted array
            int min_idx = i;
            for (int j = i+1; j < n; j++)
            {
                if (arr[j] < arr[min_idx])
                {
                    min_idx = j;
                    // Swap the found minimum element with the first
                    // element
                    int temp = arr[min_idx];
                    arr[min_idx] = arr[i];
                    arr[i] = temp;
                    if (i == 5){
                        printInt(arr); //End of X pass
                    }
                }
            }
        }
    }
    public static void printInt(int [] array) {
        for (int row = 0; row<array.length; row++){
            System.out.print(array[row] + "\t");
            }
        System.out.println();
        }




}
