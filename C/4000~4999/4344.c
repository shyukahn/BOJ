#include <stdio.h>

double getratio(void);

int main(void) {
    int n;
    scanf("%d\n", &n);
    for (int i=0; i<n; i++) {
        printf("%.3f%%\n", 100 * getratio());
    }
}

double getratio(void) {
    int num;
    scanf("%d", &num);
    int scores[num], sum=0;
    for (int i=0; i<num; i++) {
        scanf("%d", &scores[i]);
        sum += scores[i];
    }
    int avg = (double) sum / num;
    int high = 0;
    for (int i=0; i<num; i++) {
        if (scores[i] > avg) {
            high++;
        }
    }
    return (double) high / num;
}