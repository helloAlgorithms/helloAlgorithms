#include <stdio.h>
#include <stdlib.h>

int
cmp(const void* a, const void* b) {
  return *(const int*)a > *(const int*)b ? 1 : -1;
}

int
main(void) {
  int n, l, i, p[1000], s, k;
  scanf("%d %d", &n, &l);
  for (i = 0; i < n; ++i)
    scanf("%d", &p[i]);
  qsort(p, n, sizeof(int), cmp);
  s = -l - 1;
  k = 0;
  for (i = 0; i < n; ++i) {
    if (s + l <= p[i]) {
      ++k;
      s = p[i];
    }
  }
  printf("%d", k);
  return 0;
}
