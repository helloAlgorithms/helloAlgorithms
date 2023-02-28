#include <stdio.h>

int
getSum(void) {
  int i, j, k;
  int arr[5];
  int s;
  for (i = 0; i < 5; ++i)
    scanf("%d", &arr[i]);
  s = -1;
  for (i = 0; i < 3; ++i) {
    for (j = i + 1; j < 4; ++j) {
      for (k = j + 1; k < 5; ++k) {
        if (s < (arr[i] + arr[j] + arr[k]) % 10)
          s = (arr[i] + arr[j] + arr[k]) % 10;
      }
    }
  }
  return (s);
}

int
main(void) {
  int n;
  int currSum;
  int maxSum;
  int maxIdx;
  int i;

  scanf("%d", &n);
  maxSum = -1;
  maxIdx = -1;
  for (i = 0; i < n; ++i) {
    currSum = getSum();
    if (maxSum <= currSum) {
      maxIdx = i + 1;
      maxSum = currSum;
    }
  }
  printf("%d\n", maxIdx);
  return (0);
}
