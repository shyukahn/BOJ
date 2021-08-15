#include <stdio.h>

int main() {
    int a, b, c, count[10] = {0}, digits=0;
    scanf("%d%d%d", &a, &b, &c);
    int n = a*b*c, temp_n = n;
    while (temp_n > 0) {
        temp_n /= 10;
        digits++;
    }
    for (int i=0; i<digits; i++) {
        count[n%10]++;
        n /= 10;
    }
    for (int i=0; i<10; i++) {
        printf("%d\n", count[i]);
    }
}