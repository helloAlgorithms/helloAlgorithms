#include <stdio.h>
#include <stdlib.h>

int
cmp(const void* a, const void* b) {
  return *(const int*)a > *(const int*)b ? -1 : 1;
}

int
main(void) {
  int n, i, sum;
  int arr[100000];
  scanf("%d", &n);
  for (i = 0; i < n; ++i)
    scanf("%d", &arr[i]);
  qsort(arr, n, sizeof(int), cmp);
  sum = 0;
  for (i = 0; i < n; ++i) {
    if (i % 3 == 2)
      continue;
    sum += arr[i];
  }
  printf("%d", sum);
  return 0;
}
