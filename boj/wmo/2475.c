#include <stdio.h>
#include <math.h>

int main() {

	int n;
	int result = 0;
	for (int i = 0; i < 5; i++) {
		scanf("%d", &n);
		result += pow(n, 2);
	}
	printf("%d\n", result % 10);
	return 0;
}
