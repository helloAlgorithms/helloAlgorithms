#include <stdio.h>

#define MOD 1000000000
int dp[5001];

int
main(void) {
  int n, k, i;
  scanf("%d %d", &n, &k);
  dp[0] = 1;
  while (k--)
    for (i = 1; i <= n; ++i)
      dp[i] = (dp[i] + dp[i - 1]) % MOD;
  printf("%d", dp[n]);
  return 0;
}
