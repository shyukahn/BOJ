package BOJ_17213;

import java.util.*;

public class Main {
	public int frac(int n) {
		int result = 1;
		for (int i=1; i<=n; i++) {
			result *= i;
		}
		return result;
	}
	
	public static void main(String[] args) {
		Main myMain = new Main();
		Scanner s = new Scanner(System.in);
		int n = s.nextInt(), m = s.nextInt();
		s.close();
		long r = 1;
		for (int i=1; i<=n-1; i++) {
			r *= m-i;
		}
		long ans = r/myMain.frac(n-1);
		System.out.println(ans);
	}
}
