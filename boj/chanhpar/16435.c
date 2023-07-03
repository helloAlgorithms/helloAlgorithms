#include <stdio.h>
#include <stdlib.h>

int
cmp(const void* a, const void* b) {
  return *(const int*)a > *(const int*)b ? 1 : -1;
}

int
main(void) {
  int n, l, i;
  int h[1000];
  scanf("%d %d", &n, &l);
  for (i = 0; i < n; ++i)
    scanf("%d", &h[i]);
  qsort(h, n, sizeof(int), cmp);
  i = 0;
  while (i < n && h[i++] <= l)
    ++l;
  printf("%d", l);
  return 0;
}
