package BOJ_1076;

import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		String[] colors = new String[3];
		int[][] numbers = new int[3][2];
		colors[0] = s.next();
		colors[1] = s.next();
		colors[2] = s.next();
		s.close();
		long ans;
		for (int i=0; i<3; i++) {
			switch (colors[i]) {
			case "black": numbers[i][0]=0; numbers[i][1]=1; break;
			case "brown": numbers[i][0]=1; numbers[i][1]=10; break;
			case "red": numbers[i][0]=2; numbers[i][1]=100; break;
			case "orange": numbers[i][0]=3; numbers[i][1]=1000; break;
			case "yellow": numbers[i][0]=4; numbers[i][1]=10000; break;
			case "green": numbers[i][0]=5; numbers[i][1]=100000; break;
			case "blue": numbers[i][0]=6; numbers[i][1]=1000000; break;
			case "violet": numbers[i][0]=7; numbers[i][1]=10000000; break;
			case "grey": numbers[i][0]=8; numbers[i][1]=100000000; break;
			case "white": numbers[i][0]=9; numbers[i][1]=1000000000; break;
			}
		}
		int n1=numbers[0][0], n2=numbers[1][0], n3=numbers[2][1];
		ans = (long) ((10*n1)+n2)*n3;
		System.out.println(ans);
	}
}
