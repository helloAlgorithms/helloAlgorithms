#include <stdio.h>

int
main(void) {
  long x, y, z, a, b;
  scanf("%ld %ld", &x, &y);

  z = (100 * y) / x;
  if (z >= 99) {
    printf("-1\n");
  } else {
    a = (z + 1) * x - 100 * y;
    b = 99 - z;
    printf("%ld\n", a / b + (a % b != 0));
  }
  return (0);
}
