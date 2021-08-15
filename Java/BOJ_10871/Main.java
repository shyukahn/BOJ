package BOJ_10871;

import java.util.Scanner;
import java.util.ArrayList;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		ArrayList<Integer> list = new ArrayList<Integer>();
		ArrayList<Integer> ans = new ArrayList<Integer>();
		int n = sc.nextInt();
		int x = sc.nextInt();
		for (int i=0; i<n; i++) {
			list.add(sc.nextInt());
		}
		sc.close();
		for (int i: list) {
			if (i<x) {
				ans.add(i);
			}
		}
		for (int i: ans) {
			System.out.print(i+" ");
		}
	}
}
