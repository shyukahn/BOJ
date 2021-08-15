#include <stdio.h>

int getscore(void);

int main(void) {
    int n;
    scanf("%d\n", &n);
    for (int i=0; i<n; i++) {
        printf("%d\n", getscore());
    }
}

int getscore(void) {
    char ch;
    int count = 0, score = 0;
    while ((ch = getchar()) != '\n') {
        if (ch == 'O') {
            count++;
            score += count;
        } else if (ch == 'X') {
            count = 0;
        }
    }
    return score;
}