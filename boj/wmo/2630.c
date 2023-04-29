#include <stdio.h>

int arr[129][129];
int n;
int result[2];
void rec(int y, int x, int n) {

	int flag = -1;

	flag = arr[y][x];
	for (int i = y; i < y + n; i++) {
		for (int j = x; j < x + n; j++) {
			if (arr[i][j] != flag) {
				flag = -1;
				break ;
			}
		}
	}
	if (flag == -1) {
		rec(y, x, n / 2);
		rec(y + n / 2, x, n / 2);
		rec(y, x + n / 2, n / 2);
		rec(y + n / 2, x + n / 2, n / 2);
		return ;
	}
	result[flag]++;
}

int main() {

	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			scanf("%d", &arr[i][j]);
	rec(0, 0, n);
	printf("%d\n%d\n", result[0], result[1]);
	return 0;
}
