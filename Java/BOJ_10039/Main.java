package BOJ_10039;

import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		ArrayList<Integer> score = new ArrayList<Integer>();
		int sum = 0;
		for (int i=0; i<5; i++) {
			score.add(sc.nextInt());
		}
		sc.close();
		for (int i: score) {
			if (i<40) {
				i = 40;
			}
			sum += i;
		}
		System.out.println(sum/5);
	}
}
