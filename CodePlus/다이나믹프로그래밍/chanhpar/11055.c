#include <stdio.h>
#include <stdlib.h>

int
main(void) {
  int n;
  int maxSum;
  int i, j;
  int* arr;
  int* sum;
  scanf("%d", &n);
  arr = malloc(sizeof(int) * n);
  sum = malloc(sizeof(int) * n);
  for (i = 0; i < n; ++i) {
    scanf("%d", &arr[i]);
    sum[i] = arr[i];
  }

  for (i = 0; i < n; ++i) {
    for (j = 0; j < i; ++j) {
      if (arr[i] > arr[j] && sum[j] + arr[i] > sum[i])
        sum[i] = sum[j] + arr[i];
    }
    if (maxSum < sum[i])
      maxSum = sum[i];
  }

  printf("%d", maxSum);

  return (0);
}
