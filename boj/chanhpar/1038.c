#include <stdio.h>
#include <stdlib.h>

long arr[1024];
unsigned int size;

void
prepare(void) {
  int i, j;
  long num;
  for (i = 1023; i >= 1; --i) {
    num = 0;
    for (j = 9; j >= 0; --j) {
      if (i & (1L << j))
        num = num * 10 + j;
    }
    arr[size++] = num;
  }
}

int
cmp(const void* a, const void* b) {
  const long x = *(const long*)a;
  const long y = *(const long*)b;
  if (x > y)
    return (1);
  if (x < y)
    return (-1);
  return (0);
}

int
main(void) {
  unsigned int n;

  prepare();
  qsort(arr, size, sizeof(long), cmp);
  scanf("%u", &n);
  if (n >= size)
    printf("-1");
  else
    printf("%ld", arr[n]);
  return (0);
}
