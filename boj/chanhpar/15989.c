#include <stdio.h>

int
f(int n) {
  int count, m, i;
  count = n / 3 + 1;
  for (i = 0; i <= n / 3; ++i) {
    m = n - 3 * i;
    count += m / 2;
  }
  return (count);
}

int
main(void) {
  int t, n;
  scanf("%d", &t);
  while (t-- && scanf("%d", &n))
    printf("%d\n", f(n));
  return (0);
}
