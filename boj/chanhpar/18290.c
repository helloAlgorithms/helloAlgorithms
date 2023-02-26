#include <stdio.h>

int arr[100];
char visit[100];
int ans = 0x80000000;
int n, m, k, t, sum;

int
isValid(int pos) {
  int row, col;
  row = pos / m;
  col = pos % m;
  if (row - 1 >= 0 && visit[(row - 1) * m + col])
    return (0);
  if (row + 1 < n && visit[(row + 1) * m + col])
    return (0);
  if (col - 1 >= 0 && visit[row * m + col - 1])
    return (0);
  if (col + 1 < m && visit[row * m + col + 1])
    return (0);
  return (1);
}

void
dfs(int start, int count) {
  int i;

  if (count == k) {
    if (ans < sum)
      ans = sum;
    return;
  }

  for (i = start + 1; i < n * m; ++i) {
    if (isValid(i)) {
      visit[i] = 1;
      sum += arr[i];
      dfs(i, count + 1);
      sum -= arr[i];
      visit[i] = 0;
    }
  }
}

int
main(void) {
  int i;
  scanf("%d %d %d", &n, &m, &k);
  for (i = 0; i < n * m; ++i)
    scanf("%d", &arr[i]);
  dfs(-1, 0);
  printf("%d\n", ans);
  return (0);
}
