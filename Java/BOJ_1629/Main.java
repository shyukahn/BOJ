package BOJ_1629;

import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int a = s.nextInt(), b = s.nextInt(), c = s.nextInt();
		s.close();
		long m = a%c;
		long ans = 1;
		
		while (b>0) {
			if (b%2==1) {
				ans *= m;
				ans %= c;
			}
			m = ((m%c)*(m%c))%c;
			b /= 2;
		}
		System.out.print(ans);
	}
}
