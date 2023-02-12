#include <stdio.h>

#define MOD 1000000009

int n;

int dp[100001][3] = {{0, 0, 0}, {1, 0, 0}, {0, 1, 0}, {1, 1, 1}};

int
sum(int a, int b, int c) {
  int ret = a % MOD;
  ret = (ret + b) % MOD;
  ret = (ret + c) % MOD;
  return (ret);
}

int
cal(int k, int t) {
  if (k <= 3)
    return (dp[k][t]);
  if (dp[k][t] == 0)
    dp[k][t] = sum(0, cal(k - t - 1, (t + 1) % 3), cal(k - t - 1, (t + 2) % 3));
  return (dp[k][t]);
}

int
main(void) {
  int t;
  scanf("%d", &t);
  while (t--) {
    scanf("%d", &n);
    printf("%d\n", sum(cal(n, 0), cal(n, 1), cal(n, 2)));
  }
  return (0);
}
