
public class recursion2
{
    public static void main(String[]args)
    {
        //methodA(12.0, 3.0);
        //System.out.println(methodB(10));
        //System.out.println(methodC(10));
        //divisionCalc(10, 3);
        //power(2, 3);
        //System.out.println(power(3, 5));
        //geometric(5, 2);
        //gcd(12, 6);
        //power(1, 2);
        System.out.println(division(20, 6));
    }
    //Q1 a)
    public static double methodA (double value1, double value2){
        value1 = value2/2;
        value2 = value2*2;
        return methodA(value1,value2);
        //Not valid because there is no conditional statement to stop the call.
        //Double values so method will be called forever.
    }//method
    //Q1 b)
    public static double methodB (int value1){

        if (value1 == 1){
            return 1;
        }
        else {
            return value1*methodB(value1/2);
        }
        //valid
        //Instructions for what to do when value1 == 1 so as to prevent infinite recurrsion
    }//methodB
    //Q1 c)
    public static double methodC (int value1){

        if (value1<1){
            return 0;
        }
        else if (value1 == 1){
            return 5;
        }
        else {
            return 2*methodC(value1+1)+3;
        }
        //Valid for value1 <= 1
        //If > 1, method diverges
    }//methodC
    //Q3
    public static int power(int base, int exponent)
        {
        int ans = 0;
        if (base > 0 && exponent > 0)
        {
            ans = power((int)Math.pow(base, exponent), exponent - 1);

        }
        return ans;
    }
    public class BrokenCalc {

	static int[] result = new int[2]; //index 0 has quotient, index 2 remainder


	public static void main(String[] args) {
		int[]answer = practice2_Q2(19, 7);

		System.out.println(answer[0] );
		System.out.println(answer[1] );
		}

	public static  int[] practice2_Q2(int dividend, int divisor) {


		if (dividend < divisor&& dividend >=0){

			result[1] = dividend;

			return result;

			}

		else {
			result[0]+=1;
			result[1] = dividend;

			re



}
