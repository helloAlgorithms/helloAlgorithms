#include <stdio.h>

long
fn(long n, long a, long b, long c, long d, long e) {
  if (n < 6)
    return (e);
  return (fn(n - 1, b, c, d, e, 1 + d + c - a));
}

int
main(void) {
  int n;
  scanf("%d", &n);
  if (n < 6)
    printf("%d\n", n);
  else
    printf("%ld\n", fn(n, 1, 2, 3, 4, 5));
  return (0);
}
