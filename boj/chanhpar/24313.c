#include <stdio.h>

int
main(void) {
  int a1, a0, c, n;
  scanf("%d %d %d %d", &a1, &a0, &c, &n);
  printf("%d", (c > a1 && a1 * n + a0 <= c * n) || (c == a1 && a0 <= 0));
  return 0;
}
