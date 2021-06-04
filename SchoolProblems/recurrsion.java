public class recurrsion {
    public static void main(String[] args)
    {
        //System.out.println(1/10);

    //showRecursion(3);
    //methodQ1(50, 8);
    methodQ2(12345);
    }

    public static void methodQ2 (int num){
        if(num>0){

            System.out.println(num);
            methodQ2(num/10);
        }

}

    public static void showRecursion(int num)
    {
        System.out.println("Entering method. num ="+num);
        if (num>1)
        {
            showRecursion(num-1);
        }
        System.out.println("Leaving method. num ="+num);

    }

    public static void methodQ1 (int value1, int value2){
        if(value1>=value2)
        {

            methodQ1(value1/value2, value2);
        }

        System.out.print(value1%value2);
    }
}
