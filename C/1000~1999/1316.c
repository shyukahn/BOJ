#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int check(char *str) {
    if (strlen(str) <= 2) return 1;

    int chars[26];
    char *oldc = str, *c = str;
    for (int i=0; i<26; i++) {
        chars[i] = 0;
    }
    chars[*c - 'a'] = 1;
    while (1) {
        oldc = c;
        while (*c == *oldc) {
            c++;
        }
        if (*c == 0) return 1;
        if (chars[*c - 'a'] == -1) return 0;
        chars[*oldc - 'a'] = -1;
        chars[*c - 'a'] = 1;
    }

    return 1;
}

int main(void) {
    int n, cnt=0;
    char *str = malloc(101);

    scanf("%d", &n);
    for (int i=0; i<n; i++) {
        scanf("%s", str);
        if (check(str)) cnt++;
    }
    printf("%d", cnt);
    return 0;
}