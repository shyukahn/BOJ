#include <stdio.h>

int main(void)
{
    int scores[5], a, i;
    for (i = 0; i < 5; i++) {
        scanf("%d", &a);
        scores[i] = a < 40 ? 40 : a;
    }
    printf("%d\n", (scores[0] + scores[1] + scores[2] + scores[3] + scores[4]) / 5);

    return 0;
}