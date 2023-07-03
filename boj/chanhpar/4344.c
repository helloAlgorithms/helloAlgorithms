#include <stdio.h>

void
a(void) {
  int n, i, s, d;
  int b[1000];
  double c;

  scanf("%d", &n);
  s = 0;
  for (i = 0; i < n; ++i) {
    scanf("%d", &b[i]);
    s += b[i];
  }
  c = (double)s / n;
  d = 0;
  for (i = 0; i < n; ++i) {
    if ((double)b[i] > c)
      ++d;
  }
  printf("%.3f%%\n", (double)(100 * d) / n);
}

int
main(void) {
  int c;
  scanf("%d", &c);
  while (c-- > 0)
    a();
}
