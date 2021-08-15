#include <stdio.h>

int main(void)
{
    int input[10], i, re[42] = { 0 }, ans = 0;;
    for (i = 0; i < 10; i++) {
        scanf("%d", &input[i]);
        re[input[i] % 42]++;
    }
    for (i = 0; i < 42; i++) {
        if (re[i] > 0) {
            ans++;
        }
    }
    printf("%d\n", ans);

    return 0;
}