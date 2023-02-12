#include <stdio.h>
#include <stdlib.h>

int
main(void) {
  int n, i, left, right, mid, len;
  int* arr;
  int* aux;

  scanf("%d", &n);

  arr = malloc(sizeof(int) * n);
  aux = malloc(sizeof(int) * (n + 1));

  len = 0;
  aux[0] = -1;

  for (i = 0; i < n; ++i) {
    scanf("%d", &arr[i]);
    left = 1;
    right = len + 1;
    while (left < right) {
      mid = (left + right) >> 1;
      if (arr[aux[mid]] <= arr[i])
        right = mid;
      else
        left = mid + 1;
    }

    aux[left] = i;
    if (len < left)
      len = left;
  }
  printf("%d\n", len);

  return (0);
}
