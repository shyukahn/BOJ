package BOJ_2440;

import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int n = s.nextInt();
		s.close();
		for (int i=0; i<n; i++) {
			for (int j=0; j<n-i; j++) {
				System.out.print("*");
			}
			System.out.println();
		}
	}
}
