#include <stdio.h>
#include <stdlib.h>

int cmp(const void* a, const void* b) {
  const int x = *(int*)a;
  const int y = *(int*)b;
  if (x > y) return (1);
  if (x < y) return (-1);
  return (0);
}

int main(void) {
  int n, a, b, i;
  int arr[50];
  scanf("%d", &n);
  for (i = 0; i < n; ++i) {
    scanf("%d %d", &a, &b);
    arr[i] = a - b;
  }
  if (n & 1) return (printf("1\n"), 0);
  qsort(arr, n, sizeof(int), cmp);
  printf("%d\n", 1 + arr[n / 2] - arr[(n - 1) / 2]);
  return (0);
}
