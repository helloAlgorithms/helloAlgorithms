#include <stdio.h>
#include <string.h>

#define MIN(a, b) a < b ? a : b

int n;
int arr[21][21];
int d[1 << 21];
int min = 2147483647;

int dfs(int depth, int flag) {

	if (depth == n)
		return 0;
	if (d[flag] != -1)
		return d[flag];

	for (int i = 0; i < n; i++) {
		if (flag & (1 << i)) continue;
		// depth번째 일꾼이 i번째 일을 선택
		int temp = dfs(depth + 1, flag | (1 << i)) + arr[depth][i];
		if (d[flag] == -1) 
			d[flag] = temp;
		else 
			d[flag] = MIN(d[flag], temp);
	}
	return d[flag];
}

int main() {
	
	scanf("%d", &n);

	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			scanf("%d", &arr[i][j]);
	memset(d, -1, sizeof(d));
	printf("%d\n", dfs(0, 0));
	return 0;
}
