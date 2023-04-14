#include <stdio.h>

int main() {

	int n;
	int m;
	int result = 0;

	scanf("%d", &n);
	m = ~n + 1;
	n ^= m;
	for (int i = 0; i <= 32; i++)
		if (n & (1 << i))
			result++;
	printf("%d\n", result);
	return 0;
}
