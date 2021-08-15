#include <stdio.h>

int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    int b1 = b % 10;
    int b10 = (b / 10) % 10;
    int b100 = b / 100;
    printf("%d\n%d\n%d\n%d\n", a*b1, a*b10, a*b100, a*b);
}