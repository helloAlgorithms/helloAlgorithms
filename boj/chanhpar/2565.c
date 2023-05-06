#include <stdio.h>
#include <stdlib.h>

typedef struct {
  int first;
  int second;
} pair;

int
cmp(const void* a, const void* b) {
  const pair x = *(const pair*)a;
  const pair y = *(const pair*)b;

  return x.first > y.first ? 1 : -1;
}

int
search(int* arr, int size, int target) {
  int left, mid, right;
  int pos;

  left = 0;
  right = size;
  pos = size;
  while (left < right) {
    mid = (left + right) / 2;
    if (arr[mid] > target) {
      pos = mid;
      right = mid;
    } else {
      left = mid + 1;
    }
  }
  return pos;
}

int
getLISlen(pair* arr, int n) {
  int save[100];
  int size, pos;
  int i;

  size = 0;
  for (i = 0; i < n; ++i) {
    pos = search(save, size, arr[i].second);
    save[pos] = arr[i].second;
    if (pos == size)
      ++size;
  }
  return size;
}

int
main(void) {
  int n;
  int i;
  pair arr[100];
  scanf("%d", &n);
  for (i = 0; i < n; ++i)
    scanf("%d %d", &arr[i].first, &arr[i].second);
  qsort(arr, n, sizeof(pair), cmp);
  printf("%d\n", n - getLISlen(arr, n));
  return 0;
}
