#include <stdio.h>

int n;
int result;

int main() {

	scanf("%d", &n);

	for (int i = 0; i <= 6; i++) {
		if (n & (1 << i))
			result++;
	}
	printf("%d\n", result);
	return 0;
}
