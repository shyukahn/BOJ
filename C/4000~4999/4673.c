#include <stdio.h>

int d(int);

int main(void) {
    int numarray[10001] = {0}, di;
    for (int i=1; i<10001; i++) {
        di = d(i);
        if (di <= 10000) {
            numarray[di]++;
        }
    }

    for (int i=1; i<10001; i++) {
        if (!numarray[i]) {
            printf("%d\n", i);
        }
    }

    return 0;
}

int d(int n) {
    int ans = n;
    while (n > 0) {
        ans += n % 10;
        n /= 10;
    }
    return ans;
}
