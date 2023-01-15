#include <stdio.h>

#define MOD 1000000000

int n, k;
int dp[201][201];

int
main(void) {
  int i, j, t;
  scanf("%d %d", &n, &k);
  for (i = 0; i <= n; ++i) {
    for (j = 1; j <= k; ++j) {
      if (i == 0 || j == 1) {
        dp[i][j] = 1;
      } else if (dp[i][j] == 0) {
        for (t = 0; t <= i; ++t) {
          dp[i][j] += dp[t][j - 1];
          dp[i][j] %= MOD;
        }
      }
    }
  }
  printf("%d\n", dp[n][k]);
  return (0);
}
