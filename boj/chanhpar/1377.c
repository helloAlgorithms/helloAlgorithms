#include <stdio.h>
#include <stdlib.h>

enum {
  FALSE,
  TRUE
};

typedef struct {
  int val;
  int idx;
} elem;

int
cmp(const void* a, const void* b) {
  const int x = (*(elem*)a).val;
  const int y = (*(elem*)b).val;

  if (x > y)
    return (1);
  if (x < y)
    return (-1);
  return (0);
}

int
main(void) {
  int n;
  elem* arr;
  int i;
  int max;
  scanf("%d", &n);
  arr = malloc(sizeof(elem) * (n + 1));
  for (i = 0; i < n; ++i) {
    scanf("%d", &arr[i].val);
    arr[i].idx = i;
  }

  max = 0;

  qsort(arr, n, sizeof(elem), cmp);
  for (i = 0; i < n; ++i) {
    if (max < arr[i].idx - i)
      max = arr[i].idx - i;
  }
  printf("%d\n", max + 1);
  return (0);
}
