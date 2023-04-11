#include <stdio.h>

int check(int a, int x, int b, int y, int c) {
	return (a * x + b * y == c);
}

int main() {

	int a, b, c, d, e, f;
	int x, y;

	scanf("%d %d %d %d %d %d", &a, &b, &c, &d, &e, &f);
	for (int i = -999; i < 1000; i++) {
		for (int j = -999; j < 1000; j++) {
			if (check(a, i, b, j, c) && \
					check(d, i, e, j, f)) {
				printf("%d %d\n", i, j);
				return 0;
			}
		}
	}
	return 0;
}
