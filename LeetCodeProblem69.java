import java.util.*;
public class peepee {

	public static void main(String[] args) {
		Scanner input = new Scanner (System.in);
		int x = input.nextInt();
		intSqrt(x);
	}
	
	public static void intSqrt(int x) {
		System.out.println(Math.floor(Math.sqrt(x)));
	}
}