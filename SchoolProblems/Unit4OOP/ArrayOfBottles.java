//Abhinav Ramesh
//ICS4U0
//April 19th, 2021
//Questions 1-3 on slide 9 of the Array of Objects slide deck
import java.util.*;
public class ArrayOfBottles
{   //Main method
    public static void main(String[]args)
    {   //Q1
        WaterBottle[]myBottles = new WaterBottle[8];

        //Q2
        for (int i = 0; i < myBottles.length; i++)
        {
            myBottles[i] = new WaterBottle();
        }


    }
    //3a
    //Takes the WaterBottle array as input and returns the total volume of all the bottles
    public static double totalVolume(WaterBottle[] bottles)
    {
        double totalVolume = 0;
        //For every bottle in WaterBottle
        for (int i = 0; i < bottles.length; i++)
        {   //Add the volume of bottle to totVol
            totalVolume += bottles[i].volume2();
        }
        //Return total volume
        return totalVolume;
    }
    //3b
    //This method makes all the bottles which are not at prime indicies 'non-existant' by making the radius and height of the bottle 0
    public static void pourItOut(WaterBottle[] bottles)
    {
        /*Hypothetical mathematician wants to pour out all bottles that aren't at
          an index which is a prime number*/
          for (int i = 0; i < bottles.length; i++)
          {
              if (isPrime(i) == true)
              {//mathematician loves the bottle because it is at a prime index
                System.out.println("'I LOVE bottle number: " + i + "' - Your friendly neighbourhood mathematician");
              }
              //Angry mathematician sets radius and height to 0, effectively making the bottle non-existent
              else
              {
                  bottles[i].setBottleHeight(0);
                  bottles[i].setBottleRadius(0);
                  System.out.println("'I HATE your bottle :(' - Your friendly neighbourhood mathematician");
              }
          }

    }


    //3c
    /*Metal waterbottles are in higher demand due their high thermal capacity, strength, and health safety as
      compared to other materials. Let's search our array for metal bottles. */
    public static int iWantMetalBottles(WaterBottle[] bottles)
    {   //Counter to keep track of number of metal bottles
        int counter = 0;
        //Iterating through the entire array
        for (int i = 0; i < bottles.length; i++)
        {   //If it is a metal bottle
            if (bottles[i].getMaterialType() == "metal")
            {   //Print to user. i+1 because indices start at 0, but aisles make more sense if they start at 1
                System.out.println("We have a metal water bottle in aisle number " + (i+1) );
                counter++; //Add to counter if metal bottle found
            }
        }
        //Telling user total number of metal bottles
        System.out.println("There is a total of " + counter + " metals bottles in stock.");
        return counter; //returning # of metal bottles
    }

    //3d
    //Customers prefer waterbottles which are closed (aka never been opened). So lets sort the bottles by open/close status.
    //This method uses the bubble sort
    public static WaterBottle[] statusSort(WaterBottle[]arr)
    {
        int n = arr.length;
        //Going through pairs of numbers
        for (int i = 0; i < n-1; i++)
        {
           for (int j = 0; j < n-i-1; j++)
           {   //If a number to left is greater than a num to the right...
               if (arr[j].capStatus > arr[j+1].capStatus)
               {
                   // swap arr[j+1] and arr[j]
                   int temp = arr[j].capStatus;
                   arr[j].capStatus = arr[j+1].capStatus;
                   arr[j+1].capStatus = temp;
               }
           }
       }
       //Return sorted array
       return arr;
    }

    //Method to detrmine if a number is prime or not. Works by checking all numbers up to 1/2 the number and seeing if the divide the number
    public static boolean isPrime(int num)
    {   //boolean variable to keep track of if the num is prime or not
        boolean isItPrime = true;
        if (num <= 1)
        {   //If less than or equal to 1, automatically not a prime num
            isItPrime = false;
            return isItPrime;
        }
        else
        {   //Checking nums up to 1/2 of number in question
            for (int i = 2; i <= (num / 2); i++)
            {   //If a factor is found...
                if (num % i == 0)
                {
                    isItPrime = false;
                    break;
                }
            }
            //Return if the num is prime or not
            return isItPrime;
        }
    }

}
