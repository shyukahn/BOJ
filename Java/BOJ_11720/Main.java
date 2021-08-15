package BOJ_11720;

import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int n = s.nextInt();
		String line = s.next();
		s.close();
		int ans = 0;
		for (int i=0; i<n; i++) {
			ans += line.charAt(i) - '0';
		}
		System.out.println(ans);
	}
}
