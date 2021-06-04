public class testing
{
    public static void main(String[]args)
    {
        String[] ourList = {"Cool", "Apple", "Cat", "Catt", "Dog", "Ball", "Great","Excellent", "YoYo", "Water"};

        for (int i = 0; i < insertionSort(ourList).length; i++)
        {
            System.out.print(insertionSort(ourList)[i] + " ");
        }


    }

    public static String[] insertionSort (String[]yourArray)
    {
      for (int i = 1; i < yourArray.length; i++)
      {
          String currentWord = yourArray[i];
          int j;
          for (j = i - 1; j >= 0 && currentWord.compareTo(yourArray[j]) <= 0; j--)
          {
              yourArray[j + 1] = yourArray[j];
          }

          yourArray[j + 1] = currentWord;
      }
      return yourArray;
    }
    public static String[] bubbleSort (String[]oneD)
    {
        String temp;
	    for (int index1 = 0; index1<oneD.length; index1++){
	        for (int index2 = 1; index2<oneD.length; index2++){
				if (oneD[index2].compareTo(oneD[index2-1]) <= 0){
                    temp = oneD[index2-1];
                    oneD[index2-1] = oneD[index2];
                    oneD[index2]  = temp;


			}//if



		}//for index2


	}//for index1
    return oneD;
    }
}
