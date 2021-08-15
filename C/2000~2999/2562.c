#include <stdio.h>

int main() {
    int max = 0, maxi, input;
    for (int i=0; i<9; i++) {
        scanf("%d", &input);
        if (input > max) {
            max = input;
            maxi = i + 1;
        }
    }
    printf("%d\n%d", max, maxi);
}