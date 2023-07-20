#include <stdio.h>

#define MIN(a, b) a < b ? a : b

int n, m;
int arr[11][11];
int min = 2147483647;
int d[11];
int result;

void dfs(int depth, int flag, int c) {
	if (depth == m) {
		if (flag == result)
			min = MIN(c, min);
		return ;
	}
	dfs(depth + 1, flag | d[depth], c + 1);
	dfs(depth + 1, flag, c);
}

int main() {

	int t;
	scanf("%d %d", &n, &m);
	for (int i = 1; i <= n; i++)
		result |= (1 << i);
	for (int i = 0; i < m; i++) {
		scanf("%d" ,&t);
		for (int j = 0; j < t; j++) {
			scanf("%d", &arr[i][j]);
			d[i] |= (1 << (arr[i][j]));
		}
	}
	dfs(0, 0, 0);
	if (min == 2147483647)
		printf("-1\n");
	else
		printf("%d\n", min);
	return 0;
}
