#include <stdio.h>

int n, sum, idx, max;
int arr[8];
int buff[8];
char visit;

void
dfs(void) {
  int i, diff;
  if (idx == n) {
    if (sum > max)
      max = sum;
    return;
  }
  for (i = 0; i < n; ++i) {
    if (visit & (1 << i))
      continue;
    visit |= 1 << i;
    buff[idx] = arr[i];
    if (idx) {
      diff = buff[idx] - buff[idx - 1];
      if (diff < 0)
        diff = -diff;
      sum += diff;
    } else
      diff = 0;
    ++idx;
    dfs();
    sum -= diff;
    --idx;
    visit &= ~(1 << i);
  }
}

int
main(void) {
  int i;
  scanf("%d", &n);
  for (i = 0; i < n; ++i)
    scanf("%d", &arr[i]);
  dfs();
  printf("%d\n", max);
  return (0);
}
