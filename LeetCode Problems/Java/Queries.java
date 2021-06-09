import java.lang.Math;
public class Queries
{
    public static void main(String[]args)
    {
        int [][] points = {{1,1},{2,2},{3,3},{4,4},{5,5}};
        int[][] queries = {{1,2,2},{2,2,2},{4,3,2},{4,3,3}};
        System.out.println(ans(points, queries));
    }

    public static int[] ans(int[][]points, int[][]queries)
    {   //Going through each circle
        int ans[] = new int [queries.length];
        int ansIndexCounter = 0;
        for (int i = 0; i < queries.length; i++)
        {   int totalPointsInCircle = 0;
            int radius = queries[i][2];
            //Going through each point
            for (int x = 0; x < points.length; x++)
            {   //int totalPointInCircle = 0
                double distance = Math.sqrt((points[x][0] - queries[i][0])*(points[x][0] - queries[i][0]) + (points[x][1] - queries[i][1])*(points[x][1] - queries[i][1]));
                if (distance <= radius)
                {
                    totalPointsInCircle += 1;
                }
            }
            ans[ansIndexCounter] = totalPointsInCircle;
            ansIndexCounter += 1;
        }
        return ans;
    }

}
