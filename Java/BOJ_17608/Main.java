package BOJ_17608;

import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int n = s.nextInt();
		int[] height = new int[n];
		for (int i=0; i<n; i++) {
			height[i] = s.nextInt();
		}
		s.close();
		int ans = 1;
		int maxheight = height[n-1];
		for (int i=n-2; i>=0; i--) {
			if (height[i]>maxheight) {
				ans++;
				maxheight = height[i];
			}
		}
		System.out.println(ans);
	}
}
