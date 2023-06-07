#include <stdio.h>

int
main(void) {
  int n, i, maxCost, sum, limit;
  int left, right, mid;
  int arr[10000];

  scanf("%d", &n);
  maxCost = 0;
  for (i = 0; i < n; ++i) {
    scanf("%d", &arr[i]);
    if (arr[i] > maxCost)
      maxCost = arr[i];
  }
  scanf("%d", &limit);

  left = 0;
  right = maxCost + 1;
  while (left < right) {
    mid = (left + right) / 2;
    sum = 0;
    for (i = 0; i < n; ++i) {
      sum += (arr[i] < mid ? arr[i] : mid);
    }
    if (sum <= limit) {
      maxCost = mid;
      left = mid + 1;
    } else
      right = mid;
  }

  printf("%d", maxCost);
  return 0;
}
