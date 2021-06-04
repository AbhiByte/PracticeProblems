import java.util.*;
public class testtt
{
    public static void main (String[]args)
    {
        //int[][] hi = {{5, 7},{10, 4}};

        //getIndexofArray(hi);
        boolean drink = true;
        if (drink == true)
        {
            System.out.print(drink);
        }

    }

    public static void print(int n) {
   for (int i = 0; i < n; i++) {
     for (int k = 0; k < n - i; k++) {
       System.out.print(" "); // print space for triangle like structure
     }
     for (int j = 0; j <= i; j++) {
       System.out.print(pascal(i, j) + " ");
     }
     System.out.println();
   }
 }

 public static int pascal(int i, int j) {
   if (j == 0 || j == i) {
     return 1;
   } else {
     return pascal(i - 1, j - 1) + pascal(i - 1, j);
   }
 }

 public static int[] getIndexofArray (int[][]array)
 {
     int xPos = 0;
     int yPos = 0;
     for (int i = 0; i < array.length; i++)
     {
         for (int j = 0; j < array[i].length; j++)
         {
             if (array[i][j] == 10)
             {
                 xPos = i;
                 yPos = j;
             }
         }
     }
     int[] currPos = {xPos, yPos};
     return currPos;

 }

}
