#include <stdio.h>
#include <stdlib.h>

long
s(long const a) {
  return a * a;
}

void
e(long* a, long* b) {
  const long t = *a;
  if (*a > *b) {
    *a = *b;
    *b = t;
  }
}

long
d(int const (*p)[2], int const a, int const b) {
  return s(p[a][0] - p[b][0]) + s(p[a][1] - p[b][1]);
}

int
cmp(const void* a, const void* b) {
  return *(const long*)a > *(const long*)b ? 1 : -1;
}

int
c(int const (*p)[2]) {
  long a[6];
  a[0] = d(p, 0, 1);
  a[1] = d(p, 0, 2);
  a[2] = d(p, 0, 3);
  a[3] = d(p, 1, 2);
  a[4] = d(p, 1, 3);
  a[5] = d(p, 2, 3);
  qsort(a, 6, sizeof(long), cmp);
  return a[0] == a[1] && a[1] == a[2] && a[2] == a[3] && a[3] < a[4]
         && a[4] == a[5];
}

int
main(void) {
  int t, i;
  int p[4][2];
  scanf("%d", &t);
  while (t-- > 0) {
    for (i = 0; i < 4; ++i)
      scanf("%d %d", &p[i][0], &p[i][1]);
    printf("%d\n", c(p));
  }
  return 0;
}
