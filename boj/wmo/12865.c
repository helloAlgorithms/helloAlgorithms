#include <stdio.h>
#define max(a, b) a > b ? a : b;

int d[102][100010];
int v[102];
int w[102];

int n;
int k;
int result;

int main() {
    scanf("%d %d", &n, &k);

    for (int i = 1; i <= n; ++i) {
        scanf("%d %d", &w[i], &v[i]);
    }

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= k; ++j) {
            if (j - w[i] >= 0) {
                d[i][j] = max(d[i-1][j], d[i-1][j-w[i]] + v[i]);
            }
            else d[i][j] = d[i-1][j];
            if (result < d[i][j]) result = d[i][j];
        }
    }
	for (int i = 0; i <= n; i++) {
		for (int j = 0; j <= k; j++) {
			printf("%d ", d[i][j]);
		}
		printf("\n");

	}

    printf("%d", result);
    return 0;
}
