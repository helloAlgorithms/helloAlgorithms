#include <stdio.h>
#include <math.h>

int main() {

	int n;
	int a, b;

	scanf("%d", &n);
	while (n--) {
		scanf("%d %d", &a, &b);
		b %= 4;
		if (b == 0)
			b = 4;
		if (a % 10 == 0)
			printf("%d\n", 10);
		else
			printf("%d\n", (int)pow(a, b) % 10);
	}
	return 0;
}
