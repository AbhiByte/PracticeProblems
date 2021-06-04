public class calendar
{
    public static void main (String[]args)
    {
        modifiedPrintArray.print(verySimpleCalendar("january", getCalendar("january")));
    }
    //Method to get the size of our calendar given the month
    public static int[][] getCalendar (String month)
    {

        if (month.toLowerCase() == "february")
        {
            int [][] calendar = new int [4][7];
            return calendar;
        }
        else
        {
            int [][] calendar = new int [5][7];
            return calendar;
        }
    }
    //Method to fill our calendar array with all the days of the month
    public static int[][] verySimpleCalendar(String month, int[][]calendar)
    {
        int days = 0;
        int counter = 1;
        //Getting number of days based on the month
        if (month.toLowerCase() == "february")
        {
            days = 28;
        }
        if (month.toLowerCase() == "january" || month.toLowerCase() == "march" || month.toLowerCase() == "may" || month.toLowerCase() == "july" || month.toLowerCase() == "august" || month.toLowerCase() == "october" || month.toLowerCase() == "december")
        {
            days = 31;

        }
        if (month.toLowerCase() == "april" || month.toLowerCase() == "june" || month.toLowerCase() == "september" || month.toLowerCase() == "november")
        {
            days = 30;

        }
        //Filling array
        for (int i = 0; i < calendar.length; i++)
        {
            for (int j = 0; j < calendar[i].length; j++)
            {
                if (counter < days)
                {
                    calendar[i][j] = counter;
                    counter++;
                }
            }
        }
        return calendar;
    }

}
