#include <stdio.h>

int dp[501];

int
countPalinPatition(n) {
  if (n == 0)
    return (1);
  if (dp[n] == 0) {
    dp[n] = countPalinPatition(n >> 1) + countPalinPatition(n - 1);
  }
  return (dp[n]);
}

void
TC(void) {
  int n;
  scanf("%d", &n);
  printf("%d\n", countPalinPatition(n >> 1));
}

int
main(void) {
  int t;
  scanf("%d", &t);
  while (t-- > 0)
    TC();
  return (0);
}
