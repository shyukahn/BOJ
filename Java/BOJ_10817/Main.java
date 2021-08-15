package BOJ_10817;

import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		ArrayList<Integer> num = new ArrayList<Integer>();
		num.add(sc.nextInt());
		num.add(sc.nextInt());
		num.add(sc.nextInt());
		sc.close();
		int max = Math.max(Math.max(num.get(0),num.get(1)),num.get(2));
		int min = Math.min(Math.min(num.get(0),num.get(1)),num.get(2));
		for (int i=0; i<3; i++) {
			if (num.get(i)==max) {
				num.remove(i);
				break;
			}
		}
		if (num.get(0)==min) {
			System.out.println(num.get(1));
		} else {
			System.out.println(num.get(0));
		}
	}
}
