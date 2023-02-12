#include <stdio.h>

#define MOD 1000000007

long dp[5001];

long
catalan(int l) {
  int i;

  if (dp[l] == 0) {
    for (i = 0; i < l; ++i) {
      dp[l] += (catalan(i) * catalan(l - 1 - i)) % MOD;
      dp[l] %= MOD;
    }
  }
  return (dp[l]);
}

int
main(void) {
  int t, l;
  scanf("%d", &t);
  dp[0] = 1;
  while (t--) {
    scanf("%d", &l);
    if (l % 2)
      printf("0\n");
    else
      printf("%ld\n", catalan(l >> 1));
  }
  return (0);
}
