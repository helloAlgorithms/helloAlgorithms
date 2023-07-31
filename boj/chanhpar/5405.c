#include <math.h>
#include <stdio.h>

int x(int, int);
int y(int, int);

int x(int n, int addr) {
  int p, q, r;
  if (n == 1)
    return addr >= 2;
  p = 1 << (n - 1);
  q = addr / (p * p);
  r = addr % (p * p);

  switch (q) {
    case 0:
      return y(n - 1, r);
    case 1:
      return x(n - 1, r);
    case 2:
      return p + x(n - 1, r);
    default:
      return 2 * p - 1 - y(n - 1, r);
  }
}

int
y(int n, int addr) {
  int p, q, r;
  if (n == 1)
    return addr == 1 || addr == 2;
  p = 1 << (n - 1);
  q = addr / (p * p);
  r = addr % (p * p);

  switch (q) {
    case 0:
      return x(n - 1, r);
    case 1:
      return p + y(n - 1, r);
    case 2:
      return p + y(n - 1, r);
    default:
      return p - 1 - x(n - 1, r);
  }
}

void
test(void) {
  int n, h, o;
  long a, b;
  scanf("%d %d %d", &n, &h, &o);
  a = 10 * (x(n, h - 1) - x(n, o - 1));
  b = 10 * (y(n, h - 1) - y(n, o - 1));
  printf("%d\n", (int)round(sqrt(a * a + b * b)));
}

int
main(void) {
  int t;
  scanf("%d", &t);
  while (t-- > 0)
    test();
  return 0;
}
