#include <stdio.h>

int
gcd(int a, int b) {
  int c;
  while ((c = a % b)) {
    a = b;
    b = c;
  }
  return b;
}

int
main(void) {
  int g, l, p, t;
  scanf("%d %d", &g, &l);
  l /= g;
  t = 1;
  for (p = 1; p < l / p; ++p) {
    if (l % p == 0 && gcd(p, l / p) == 1)
      t = p;
  }
  printf("%d %d", g * t, g * (l / t));
  return 0;
}
