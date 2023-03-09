#include <stdio.h>
#include <stdlib.h>

int arr[200000];
int n;

int
cmp(const void* a, const void* b) {
  const int x = *(const int*)a;
  const int y = *(const int*)b;

  if (x > y)
    return (1);
  if (x < y)
    return (-1);
  return (0);
}

int
whereis(int d) {
  int left, right, mid;
  int ans;

  left = 0;
  right = n;
  ans = -1;
  while (left < right) {
    mid = (left + right) / 2;
    if (arr[mid] >= d) {
      right = mid;
      if (arr[mid] == d)
        ans = mid;
    } else {
      left = mid + 1;
    }
  }
  return (ans);
}

int
main(void) {
  int m, d;
  int i;
  scanf("%d %d", &n, &m);
  for (i = 0; i < n; ++i)
    scanf("%d", &arr[i]);
  qsort(arr, n, sizeof(int), cmp);
  for (i = 0; i < m; ++i) {
    scanf("%d", &d);
    printf("%d\n", whereis(d));
  }
  return (0);
}
