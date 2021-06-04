public class geometric{
    public static void main(String[]args){

        System.out.println(power(3, 2, 5));
    }//main

    public static int power(int num, int ratio, int termNum)
    {
        int counter = 0;

        if (termNum == 1)
        {
            return num;
        }
        else
        {
            return  ratio*power(num, ratio, termNum-1);
        }
    }

}
