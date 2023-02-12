#include <stdio.h>

enum {
  FALSE,
  TRUE
};

int
max(int a, int b) {
  return (a > b ? a : b);
}

int n;
int arr[10001];

/* int dp[10001][2]; */

int
main(void) {
  int a, b, c, d, e;
  int i;
  scanf("%d", &n);
  for (i = 1; i <= n; ++i)
    scanf("%d", &arr[i]);
  e = 0;
  c = 0;
  d = arr[1];
  for (i = 2; i <= n; ++i) {
    a = max(c, d);
    b = arr[i] + max(c, e + arr[i - 1]);
    e = c;
    c = a;
    d = b;
  }
  printf("%d\n", max(c, d));
  return (0);
}

/* dp[1][FALSE] = 0; */
/* dp[1][TRUE] = arr[1]; */
/* dp[i][FALSE] = max(dp[i - 1][FALSE], dp[i - 1][TRUE]); */
/* dp[i][TRUE] = arr[i] + max(dp[i - 1][FALSE], dp[i - 2][FALSE] + arr[i - 1]);
 */
/* printf("%d\n", max(dp[n][TRUE], dp[n][FALSE])); */
