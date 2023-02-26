#include <stdio.h>

int dp[2000][2000];
int arr[2000];

int
max(int a, int b) {
  return (a > b ? a : b);
}

int
solve(int s, int e, int c) {
  if (s == e)
    return (c * arr[s]);
  if (dp[s][e] == 0) {
    dp[s][e] = max(c * arr[e] + solve(s, e - 1, c + 1),
                   c * arr[s] + solve(s + 1, e, c + 1));
  }
  return (dp[s][e]);
}

int
main(void) {
  int n;
  int i;

  scanf("%d", &n);
  for (i = 0; i < n; ++i) {
    scanf("%d", &arr[i]);
  }

  printf("%d", solve(0, n - 1, 1));

  return (0);
}
