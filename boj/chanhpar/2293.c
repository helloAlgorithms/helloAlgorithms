#include <stdio.h>
#include <string.h>

int
main(void) {
  int n, k;
  int arr[100];
  int dp[10001];
  int i, j;

  scanf("%d %d", &n, &k);
  for (i = 0; i < n; ++i)
    scanf("%d", &arr[i]);
  memset(dp, 0, sizeof(int) * 10001);
  dp[0] = 1;
  for (i = 0; i < n; ++i)
    for (j = arr[i]; j <= k; ++j)
      dp[j] += dp[j - arr[i]];
  printf("%d", dp[k]);
  return 0;
}
