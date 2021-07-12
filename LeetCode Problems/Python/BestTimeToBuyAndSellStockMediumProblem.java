import java.util.ArrayList;
import java.util.*;
public class BestTimeToBuyAndSellStockMediumProblem {
    public static int getMin(int[] inputArray){
        int minValue = inputArray[0];
        for(int i = 1; i < inputArray.length; i++){ 
            if(inputArray[i] < minValue){
                minValue = inputArray[i];
          }
        }
    return minValue;
  }
    public int maxProfit(int[] prices) {

        ArrayList<Integer> myNumbers = new ArrayList<Integer>();

        int min = getMin(prices);
        if (Arrays.asList(prices).indexOf(min) == prices.length-1)
        {
            return 0;
        }
        for (int i = 0; i < prices.length; i++)
        {
            for (int j = 1; j < prices.length; j++)
            {

                 int diff = j - i;
                 myNumbers.add(diff);

            }
        }
        int max = 0;
        for (int k = 0; k < myNumbers.size(); k++)
        {
            if (myNumbers.get(k) > max)
            {
                max = myNumbers.get(k);
            }
        }
        return max;
    }
}
