#include <stdio.h>

int
main(void) {
  long n, i, p;
  scanf("%ld", &n);
  p = 1;
  for (i = 1; i <= n; ++i) {
    p *= i;
    while (p % 10 == 0)
      p /= 10;
    p %= 100000000;
  }
  printf("%ld\n", p % 10);
  return 0;
}
