//Not fully done. Logic is correct but some bug :(
import java.lang.Math;
public class Queries
{
    public static void main(String[]args)
    {

    }

    public static int[] ans(int[][]points, int[][]queries)
    {   //Going through each circle
        int ans[] = new int [queries.length];
        int ansIndexCounter = 0;
        for (int i = 0; i < queries.length; i++)
        {   int totalPointsInCircle = 0;
            radius = queries[i][2];
            //Going through each point
            for (int x = 0; x < points.length; x++)
            {   //int totalPointInCircle = 0
                distance = Math.sqrt((points[x][0] - queries[i][0])*(points[x][0] - queries[i][0]) + (points[x][1] - queries[i][1])*(points[x][1] - queries[i][1]));
                if (distance <= radius)
                {
                    totalPointsInCircle += 1;
                }
            }
            ans[ansIndexCounter] = totalPointsInCircle;
            ansIndexCounter += 1;
        }
    }

}
