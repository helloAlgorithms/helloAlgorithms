#include <stdio.h>

int main() {

	int a, b, c;

	scanf("%d %d %d", &a, &b, &c);
	if (c & (1 << 0))
		printf("%d\n", a ^ b);
	else
		printf("%d\n", a ^ b ^ b);
	return 0;
}
