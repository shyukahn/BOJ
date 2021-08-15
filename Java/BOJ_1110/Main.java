package BOJ_1110;

import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int a = n;
		int i = 1;
		sc.close();
		n = 10*(n%10)+(n/10+n%10)%10;
		while (n != a) {
			n = 10*(n%10)+(n/10+n%10)%10;
			i++;
		}
		System.out.println(i);
	}
}
