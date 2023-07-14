#include <stdio.h>

int x(int c, int d) { return c > d ? c - d : d - c; }

int main(void) {
  int a, b, n, i, m; int p[6]; int *q;
  scanf("%d %d", &a, &b); scanf("%d", &n);
  for (i = 0; i < n; ++i) { scanf("%d", &p[i]); p[i] = 1 + x(p[i], b); }
  p[n] = x(a, b);
  q = p;
  m = q[0];
  while (n-- > 0) { if (m > *++q) m = *q; }
  printf("%d", m);
  return 0;
}
