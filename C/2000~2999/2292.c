#include <stdio.h>

int main(void)
{
    int n, ans = 1, i = 1;
    scanf("%d", &n);
    n--;
    while (n > 0) {
        n -= 6 * i;
        i++;
        ans++;
    }
    printf("%d\n", ans);
    return 0;
}