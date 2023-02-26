#include <stdio.h>
#include <stdlib.h>

int n;
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

int
main(void) {
  int i;
  int total;

  scanf("%d", &n);
  for (i = 0; i < n; ++i)
    scanf("%d", &arr[i]);
  qsort(arr, n, sizeof(int), cmp);

  total = 0;
  for (i = 0; i < n; ++i) {
    if (arr[i] > total + 1) {
      break;
    }
    total += arr[i];
  }
  printf("%d\n", total + 1);
  return (0);
}
