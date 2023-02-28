#include <stdio.h>
#include <stdlib.h>

int n, s, count;
int arr[20];

int
cmp(const void* a, const void* b) {
  const int x = *(int*)a;
  const int y = *(int*)b;
  if (x > y)
    return (1);
  if (x < y)
    return (-1);
  return (0);
}

void
dfs(int start, int sum) {
  int i;
  for (i = start + 1; i < n; ++i) {
    if (sum + arr[i] == s)
      ++count;
    else if (sum + arr[i] > s && arr[i] > 0)
      return;
    dfs(i, sum + arr[i]);
  }
}

int
main(void) {
  int i;
  scanf("%d %d", &n, &s);
  for (i = 0; i < n; ++i)
    scanf("%d", &arr[i]);
  qsort(arr, n, sizeof(int), cmp);
  dfs(-1, 0);
  printf("%d\n", count);
  return (0);
}
