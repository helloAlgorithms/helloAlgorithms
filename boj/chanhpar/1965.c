#include <stdio.h>
#include <stdlib.h>

int
search(int* arr, int size, int target) {
  int left, right, mid, pos;
  left = 0;
  pos = size;
  right = size;
  while (left < right) {
    mid = (left + right) / 2;
    if (arr[mid] < target) {
      left = mid + 1;
    } else {
      pos = mid;
      right = mid;
    }
  }
  return pos;
}

int
getLISlen(int* arr, int size) {
  int* save;
  int len, pos, i;

  save = malloc(sizeof(int) * size);
  len = 0;
  for (i = 0; i < size; ++i) {
    pos = search(save, len, arr[i]);
    save[pos] = arr[i];
    if (pos == len)
      ++len;
  }
  free(save);
  return len;
}

int
main(void) {
  int n, i;
  int* arr;
  scanf("%d", &n);
  arr = malloc(sizeof(int) * n);
  for (i = 0; i < n; ++i)
    scanf("%d", &arr[i]);
  printf("%d", getLISlen(arr, n));
  free(arr);
  return 0;
}
