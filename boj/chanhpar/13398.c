#include <stdio.h>

enum {
  INCL,
  EXCL
};

int arr[100001];
int dp[100001][2];

int
max3(int a, int b, int c) {
  int m;

  m = a;
  if (m < b)
    m = b;
  if (m < c)
    m = c;
  return (m);
}

int
main(void) {
  int n, i, ans;
  scanf("%d", &n);
  scanf("%d", &arr[0]);
  dp[0][INCL] = arr[0];
  dp[0][EXCL] = arr[0];
  ans = arr[0];
  for (i = 1; i < n; ++i) {
    scanf("%d", &arr[i]);
    dp[i][INCL] = (dp[i - 1][INCL] > 0) ? arr[i] + dp[i - 1][INCL] : arr[i];
    dp[i][EXCL] = max3(dp[i - 1][INCL], arr[i], dp[i - 1][EXCL] + arr[i]);

    if (dp[i][EXCL] > ans)
      ans = dp[i][EXCL];
  }
  printf("%d\n", ans);
  return (0);
}
