#include <stdio.h>
#include <stdlib.h>

int
cmp(const void* a, const void* b) {
  return (*(const int*)a > *(const int*)b);
}

int
abs(int k) {
  return (k >= 0 ? k : -k);
}

int pair[2];
int arr[100000];
int left, right;

int
main(void) {
  int n;
  int i;
  scanf("%d", &n);
  for (i = 0; i < n; ++i)
    scanf("%d", &arr[i]);
  qsort(arr, n, sizeof(int), cmp);
  left = 0;
  right = n - 1;
  pair[0] = 0;
  pair[1] = n - 1;
  while (left < right) {
    if (abs(arr[pair[0]] + arr[pair[1]]) > abs(arr[left] + arr[right])) {
      pair[0] = left;
      pair[1] = right;
    }
    if (arr[left] + arr[right] > 0)
      --right;
    else if (arr[left] + arr[right] < 0)
      ++left;
    else
      break;
  }
  printf("%d %d\n", arr[pair[0]], arr[pair[1]]);
  return (0);
}
