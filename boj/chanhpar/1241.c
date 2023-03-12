#include <stdio.h>

#define MAX 1000000

int count[MAX + 1];
int arr[100000];

int
main(void) {
  int n;
  int i, j;
  scanf("%d", &n);
  for (i = 0; i < n; ++i) {
    scanf("%d", &arr[i]);
    count[arr[i]] += 1;
  }
  for (i = MAX; i >= 1; --i)
    for (j = i << 1; j <= MAX; j += i)
      count[j] += count[i];
  for (i = 0; i < n; ++i)
    printf("%d\n", count[arr[i]] - 1);
  return (0);
}
