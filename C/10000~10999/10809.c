#include <stdio.h>

int main(void) {
	int alphabets[26];
	for (int i = 0; i < 26; i++) {
		alphabets[i] = -1;
	}

	char str[101];
	scanf("%s", str);

	int i = 0;
	char index;
	while (str[i] != 0) {
		index = str[i] - 'a';
		if (alphabets[index] < 0) {
			alphabets[index] = i;
		}
		i++;
	}

	for (int i = 0; i < 26; i++) {
		printf("%d ", alphabets[i]);
	}
	printf("\n");

	return 0;
}
