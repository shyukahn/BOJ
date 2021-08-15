#include <stdio.h>

int main(void) {
	int n;
	scanf("%d", &n);
	int scores[n], max = 0;
	for (int i=0; i<n; i++) {
		scanf("%d", &scores[i]);
		if (scores[i] > max) {
			max = scores[i];
		}
	}
	double new_scores[n], sum = 0;
	for (int i=0; i<n; i++) {
		new_scores[i] = (double) 100*scores[i]/max;
		sum += new_scores[i];
	}
	printf("%f", sum/n);
	return 0;
}