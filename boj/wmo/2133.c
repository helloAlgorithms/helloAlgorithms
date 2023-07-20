#include <stdio.h>

int d[31];

int main() {

	int n;
	scanf("%d", &n);

	if (n & 1) {
		printf("0\n");
		return 0;
	}
	d[2] = 3;
	for (int i = 4; i <= n; i += 2) {
		d[i] += (d[i - 2] * 3) + 2;
		for (int j = i - 4; j >= 2; j -= 2) {
			d[i] += d[j] * 2;
		}
	}
	printf("%d\n", d[n]);
	return 0;
}
