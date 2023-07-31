#include <stdio.h>

#define MOD 1000000009

int dp[1001][1001];

int
f(int n, int m) {
  if (n <= 0 || m <= 0 || n > 3 * m || n < m)
    return 0;
  if (dp[n][m])
    return dp[n][m];

  if (m == 1) {
    if (n <= 3)
      dp[n][m] = 1;
    else
      return 0;
  } else {
    dp[n][m] = (dp[n][m] + f(n - 1, m - 1)) % MOD;
    dp[n][m] = (dp[n][m] + f(n - 2, m - 1)) % MOD;
    dp[n][m] = (dp[n][m] + f(n - 3, m - 1)) % MOD;
  }
  return dp[n][m];
}

int
main(void) {
  int t, n, m;
  scanf("%d", &t);
  while (t--) {
    scanf("%d %d", &n, &m);
    printf("%d\n", f(n, m));
  }
  return 0;
}
