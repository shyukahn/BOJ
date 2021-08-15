#include <stdio.h>

int main() {
    int n, min = 1000000, max = -1000000, input;
    scanf("%d", &n);
    for (int i=0; i<n; i++) {
        scanf("%d", &input);
        if (input < min) {
            min = input;
        }
        if (input > max) {
            max = input;
        }
    }
    printf("%d %d", min, max);
}