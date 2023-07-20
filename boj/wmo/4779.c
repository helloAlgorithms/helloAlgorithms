#include <stdio.h>
#include <string.h>
#include <math.h>

char arr[600000];

void rec(int x, int n) {

	if (n == 0)
		return ;
	for (int i = x + n / 3; i < x + n / 3 * 2; i++)
		arr[i] = 32;
	rec(x, n / 3);
	rec(x + n / 3, n / 3);
	rec(x + n / 3 * 2, n / 3);
}

int main() {

	int n;

	while (scanf("%d", &n) != -1) {
		n = pow(3, n);
		memset(arr, '-', sizeof(arr));
		rec(0, n);
		for (int i = 0; i < n; i++)
			printf("%c", arr[i]);
		printf("\n");
	}
	return 0;
}
