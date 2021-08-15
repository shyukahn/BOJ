#include <stdio.h>

int main() {
    int n, new_n, cycle, n10, n1;
    scanf("%d", &n);
    cycle = 0;
    new_n = n;
    do {
        cycle++;
        n10 = new_n / 10;
        n1 = new_n % 10;
        new_n = 10 * n1 + (n10 + n1) % 10;
    } while (new_n != n);
    printf("%d", cycle);
}