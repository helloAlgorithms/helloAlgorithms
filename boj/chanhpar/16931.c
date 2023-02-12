#include <stdio.h>

int
main(void) {
  int arr[100][100];
  int n, m;
  int i, j;
  int sum;
  scanf("%d %d", &n, &m);
  for (i = 0; i < n; ++i) {
    for (j = 0; j < m; ++j) {
      scanf("%d", &arr[i][j]);
    }
  }

  sum = 2 * n * m;

  for (i = 0; i < n; ++i) {
    for (j = 0; j < m; ++j) {
      if (j == 0)
        sum += arr[i][j];
      else if (arr[i][j] > arr[i][j - 1])
        sum += arr[i][j] - arr[i][j - 1];

      if (i == 0)
        sum += arr[i][j];
      else if (arr[i][j] > arr[i - 1][j])
        sum += arr[i][j] - arr[i - 1][j];

      if (j == m - 1)
        sum += arr[i][j];
      else if (arr[i][j] > arr[i][j + 1])
        sum += arr[i][j] - arr[i][j + 1];

      if (i == n - 1)
        sum += arr[i][j];
      else if (arr[i][j] > arr[i + 1][j])
        sum += arr[i][j] - arr[i + 1][j];
    }
  }

  printf("%d\n", sum);

  return (0);
}
