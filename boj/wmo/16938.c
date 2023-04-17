#include <stdio.h>

#define MIN(a, b) (a) < (b) ? (a) : (b)
#define MAX(a, b) (a) > (b) ? (a) : (b)

int n, l, r, x;
int arr[16];
int result;
void dfs(int depth, int flag, int min, int max, int c) {

	if (depth > n)
		return ;
	if (depth == n && c >= 2 && (max - min) >= x) {
		if (flag >= l && flag <= r)
			result++;
		return ;
	}
	dfs(depth + 1, flag + arr[depth], MIN(arr[depth], min), MAX(arr[depth], max), c + 1);
	dfs(depth + 1, flag, min, max, c);
}

int main() {

	scanf("%d %d %d %d", &n, &l, &r, &x);
	for (int i = 0; i < n; i++)
		scanf("%d", &arr[i]);
	dfs(0, 0, 2147483647, -2147483648, 0);
	printf("%d\n", result);
	return 0;
}
