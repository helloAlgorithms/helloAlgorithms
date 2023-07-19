#include <stdio.h>
#include <stdlib.h>

int
cmp(const void* a, const void* b) {
  return *(const int*)a > *(const int*)b ? 1 : -1;
}

int
c(const int a, const int b) {
  return a < b ? a : b;
}

int
main(void) {
  int n, m, p[1000], i, a, b;
  scanf("%d %d", &n, &m);
  for (i = 0; i < m; ++i)
    scanf("%d", &p[i]);
  qsort(p, m, sizeof(int), cmp);
  a = b = 0;
  for (i = 0; i < m; ++i) {
    if (b < p[i] * c(m - i, n)) {
      a = p[i];
      b = a * c(m - i, n);
    }
  }
  printf("%d %d", a, b);
  return 0;
}
