#include <stdio.h>

#define MOD 10007

int n;
int dp[1001][10];

int
main(void) {
  int i, j, k, sum;
  scanf("%d", &n);
  for (i = 0; i < 10; ++i)
    dp[1][i] = 1;
  for (i = 2; i <= n; ++i) {
    for (j = 0; j < 10; ++j) {
      for (k = 0; k <= j; ++k) {
        dp[i][j] += dp[i - 1][k] % MOD;
      }
      dp[i][j] %= MOD;
    }
  }
  sum = 0;
  for (i = 0; i < 10; ++i)
    sum += dp[n][i];
  printf("%d\n", sum % MOD);
  return (0);
}
