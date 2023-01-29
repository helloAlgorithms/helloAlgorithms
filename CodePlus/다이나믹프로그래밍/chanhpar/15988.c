#include <stdio.h>

#define MOD 1000000009

long dp[1000001];

void
tc(void) {
  int n;
  scanf("%d", &n);
  printf("%ld\n", dp[n]);
}

int
main(void) {
  int t, i;
  scanf("%d", &t);
  dp[1] = 1;
  dp[2] = 2;
  dp[3] = 4;

  for (i = 4; i <= 1000000; ++i) {
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MOD;
  }
  while (t--)
    tc();
  return (0);
}
