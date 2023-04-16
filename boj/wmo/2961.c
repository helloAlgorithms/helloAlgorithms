#include <stdio.h>
#include <string.h>

#define MIN(a, b) a < b ? a : b
#define ABS(x) ((x) < 0)?-(x):(x)
int n;
int arr[11][2];
int min = 2147483647;

void dfs(int depth, int flag) {

	if (depth == n) {
		if (flag == 0)
			return ;
		int a = 1;
		int b = 0;
		for (int i = 0; i < n; i++) {
			if (flag & (1 << i)) {
				a *= arr[i][0];
				b += arr[i][1];
			}
		}
		min = MIN(min, (ABS(a - b)));
		return ;
	}
	dfs(depth + 1, flag | (1 << depth));
	dfs(depth + 1, flag);
}

int main() {

	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%d %d", &arr[i][0], &arr[i][1]);
	dfs(0, 0);
	printf("%d\n", min);
}
