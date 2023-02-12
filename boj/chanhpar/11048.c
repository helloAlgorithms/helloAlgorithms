#include <stdio.h>

int board[1000][1000];
int dp[1000][1000];

int
max(int a, int b) {
  return (a > b ? a : b);
}

int
f(int x, int y) {
  if (x < 0 || y < 0)
    return (0);
  if (dp[x][y] == -1) {
    dp[x][y] = board[x][y] + max(f(x - 1, y), f(x, y - 1));
  }
  return (dp[x][y]);
}

int
main(void) {
  int n, m;
  int i, j;
  scanf("%d %d", &n, &m);
  for (i = 0; i < n; ++i) {
    for (j = 0; j < m; ++j) {
      scanf("%d", &board[i][j]);
      dp[i][j] = -1;
    }
  }
  printf("%d\n", f(n - 1, m - 1));
  return (0);
}
