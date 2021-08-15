package BOJ_2577;

import java.util.*;

public class Main {
	public int power10(int n) {
		int power = 1;
		for (int i=0; i<n; i++) {
			power *= 10;
		}
		return power;
	}
	
	public static void main(String[] args) {
		Main myMain = new Main();
		Scanner s = new Scanner(System.in);
		int a = s.nextInt(), b = s.nextInt(), c = s.nextInt();
		s.close();
		int result = a*b*c;
		int[] numbers = new int[10];
		for (int i=0; i<=Math.log10(result); i++) {
			numbers[(result%(myMain.power10(i+1)))/myMain.power10(i)] += 1;
		}
		for (int i=0; i<10; i++) {
			System.out.println(numbers[i]);
		}
	}
}
