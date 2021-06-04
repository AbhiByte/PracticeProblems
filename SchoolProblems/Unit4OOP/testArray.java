import java.util.*;
import java.util.Arrays.*;
public class testArray implements Comparable<testArray>
{
    public static void main(String[]args)
    {
        WaterBottle[] btls = new WaterBottle [8];

        for (int i = 0; i < btls.length; i++)
        {
            btls[i] = new WaterBottle();
        }
    }

    public static WaterBottle[] sortIt(WaterBottle[] oneD)
    {
            int temp;
    	    for (int index1 = 0; index1<oneD.length;index1++){
    		for(int index2 = 1;index2<oneD.length; index2++){

    			temp = oneD[index2-1].getCapStatus;
    			if(oneD[index2]<oneD[index2-1]){

    				oneD[index2-1].setCapStatus = oneD[index2].getCapStatus;
    				oneD[index2].getCapStatus = temp;


    		}//if


    		}//for index2



    	}//for index1




        }

}
