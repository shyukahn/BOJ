package BOJ_10996;

import java.util.*;

public class Main {
	public String f(int n) {
		if (n%2==0) {
			return " ";
		} else {
			return "*";
		}
	}
	public static void main(String[] args) {
		Main myMain = new Main();
		Scanner s = new Scanner(System.in);
		int n = s.nextInt();
		s.close();
		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				System.out.print(myMain.f(j+1));
			}
			System.out.println();
			for (int j=0; j<n; j++) {
				System.out.print(myMain.f(j));
			}
			System.out.println();
		}
	}
}
