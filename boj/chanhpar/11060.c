#include <stdio.h>

int n;
int maze[1000];
int dp[1000];

int
min(int a, int b) {
  return (a < b ? a : b);
}

int
main(void) {
  int i, j;
  scanf("%d", &n);
  for (i = 0; i < n; ++i) {
    scanf("%d", &maze[i]);
    dp[i] = 2000;
  }
  dp[0] = 0;
  for (i = 0; i < n; ++i) {
    for (j = 1; j <= maze[i]; ++j) {
      dp[i + j] = min(dp[i + j], 1 + dp[i]);
    }
  }
  printf("%d\n", dp[n - 1] == 2000 ? -1 : dp[n - 1]);
  return (0);
}
