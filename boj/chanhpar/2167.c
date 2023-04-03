#include <stdio.h>

int arr[301][301];

int
main(void) {
  int n, m, k;
  int i, j, x, y;
  int a, b;
  scanf("%d %d", &n, &m);
  for (a = 1; a <= n; ++a) {
    for (b = 1; b <= m; ++b) {
      scanf("%d", &arr[a][b]);
      arr[a][b] += arr[a - 1][b] + arr[a][b - 1] - arr[a - 1][b - 1];
    }
  }
  scanf("%d", &k);
  while (k--) {
    scanf("%d %d %d %d", &i, &j, &x, &y);
    printf("%d\n",
           arr[x][y] - arr[x][j - 1] - arr[i - 1][y] + arr[i - 1][j - 1]);
  }
  return (0);
}
