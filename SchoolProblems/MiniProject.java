import java.util.Random;
public class MiniProject
{
    /*
    Abhinav Ramesh
    ICS4U0
    Airline booking page with prices to a certain destination displayed in a calendar-esque format for the month of March and a hypothetical lottery discount system.
    Knowledge of 1D arrays is demonstrated with the daysOfWeek method that assigns the days of the week to a blank array.
    Knoweldge of 2D arrays is demonstarted with priceList and print methods which assign random price values to a 2D array and print them out, respectively.
    Knowledge of recursion is demonstrated with ticketLottery method that calculates the multiplicative persistence of a number.
    March 10th, 2021
    */
    public static void main (String[]args)
    {

        //Creating a calendar page to fit all airline ticket prices for March
        int[][]marchSchedule = new int [5][7];

        daysOfWeek();
        System.out.println();
        print(priceList(marchSchedule));

        int price = 3735; //Random price for demonstration
        System.out.println("The multiplicative persistence of your total travel cost is " + ticketLottery(price) + ", so you'll recieve a $" + ticketLottery(price) + "00 discount!");
    }

    //This method returns a title ("Prices for March... ") and a 1D array with the days of the week.
    public static void daysOfWeek ()
    {
        //Printing out the title
        System.out.println("Prices for March 2021 (USD)");
        //Array containing each day of the week
        String [] daysList = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};

        //Iterating through each day of the week in daysList and printing it
        for (int i = 0; i < daysList.length; i++)
        {
            System.out.print(daysList[i] + "     ");
        }
        System.out.println();
    }

    //Filling in random price values for each element (day) in the month
    public static int[][] priceList (int[][]inputArray)
    {
        //Total days in the month
        int days = 31;
        //Variable to iterate through 31 days
        int counter = 0;
        //Random method
        Random random = new Random();
        //Filling each element in the month with a random price
        for (int i = 0; i < inputArray.length; i++)
        {
            for (int j = 0; j < inputArray[i].length; j++)
            {
                if (counter < days)
                {
                    //Since March begins with Monday, Sunday which is [0][0] gets a value of 0
                    if (i == 0  && j == 0)
                    {
                        inputArray[i][j] = 0;
                    }
                    //The next 31 elements gets assigned a random price between 100 and 500
                    //Since our calendar array contains more than 32 elements, the remaining indices will recieve a value of zero
                    else
                    {
                        inputArray[i][j] = random.nextInt(500 - 100 + 1) + 100;
                        counter++;
                    }
                }
            }
        }
        return inputArray;
    }

    //Airline discount lottery where your total travel cost determines the discount on the ticket.
    //The method calculates the 'multiplicative persistence' of the travel cost.
    //multiplicative persistence is the amount of times the digits of a given number can be multiplied before becomming a single digit.
    //Example: '3735' -> '315' -> '15' -> '5' Therefore the multiplicative persistence of 3735 is 3.
    public static int ticketLottery (int totalCostOfTrip)
    {
        //If the total travel cost is less than 10, the multiplicative persistence (discount) is zero.
        if(totalCostOfTrip < 10)
        {
            return 0;
        }
        //Counter variable for keeping track of the current value of the total cost as we iterate through the loop.
        int counter = 1;
        while(totalCostOfTrip != 0)
        {
            //Goes through every single digit in the total trip cost and multiplies it with the counter.
            counter *= (totalCostOfTrip % 10);
            totalCostOfTrip /= 10;
        }
        if (counter > 10)
        {
            //Recursive call to the method for each time the counter is not a single digit number
            return 1 + ticketLottery(counter);
        }
        else
        {
            return 1;
        }

    }
    //Modified print method to print all elements of a 2D array except indices that contain a value of 0.
    public static void print(int[][]theArrayYouWantToPrint)
	{
        //Going through each element in the array
		for (int i = 0; i < theArrayYouWantToPrint.length; i++)
		{
			for (int j = 0; j < theArrayYouWantToPrint[i].length; j++)
			{
                //Print only if element != 0
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
