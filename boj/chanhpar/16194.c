#include <stdio.h>

int n;
int arr[1001];
int dp[1001];

int
min(int a, int b) {
  return (a < b ? a : b);
}

int
main(void) {
  int i, j;
  scanf("%d", &n);
  for (i = 1; i <= n; ++i) {
    scanf("%d", &arr[i]);
    dp[i] = 0x7fffffff;
  }
  for (i = 1; i <= n; ++i) {
    for (j = 0; j <= i; ++j) {
      dp[i] = min(dp[i], dp[j] + arr[i - j]);
    }
  }
  printf("%d\n", dp[n]);
  return (0);
}
