#include <stdio.h>

int dp[9][9];

int
nCr(int n, int r) {
  if (r == 0)
    return 1;
  if (dp[n][r] == 0) {
    if (r > n - r)
      dp[n][r] = nCr(n, n - r);
    else
      dp[n][r] = nCr(n - 1, r - 1) + nCr(n - 1, r);
  }
  return dp[n][r];
}

int
main(void) {
  int n, m, k, i, a, b;
  scanf("%d %d %d", &n, &m, &k);
  a = 0;
  for (i = k; i <= m; ++i) {
    if (n - m >= m - i)
      a += nCr(m, i) * nCr(n - m, m - i);
  }
  b = nCr(n, m);
  printf("%.12lf", (double)a / (double)b);
  return 0;
}
