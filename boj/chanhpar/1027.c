#include <stdio.h>

int
main(void) {
  int n;
  int arr[50];
  int count[50];
  int i, j, a, b, maxCount;
  scanf("%d", &n);
  for (i = 0; i < n; ++i) {
    scanf("%d", &arr[i]);
    count[i] = 0;
  }
  maxCount = 0;
  for (i = 0; i + 1 < n; ++i) {
    ++count[i];
    ++count[i + 1];
    a = 1;
    b = arr[i + 1] - arr[i];
    for (j = i + 2; j < n; ++j) {
      if (((double)(arr[j] - arr[i])) / (j - i) > ((double)b) / a) {
        ++count[i];
        ++count[j];
        a = j - i;
        b = arr[j] - arr[i];
      }
    }
    if (maxCount < count[i])
      maxCount = count[i];
  }
  printf("%d", maxCount > count[n - 1] ? maxCount : count[n - 1]);
  return 0;
}
