#include <math.h>
#include <stdio.h>

int
main(void) {
  double x, y, c, a, b, left, right;
  scanf("%lf %lf %lf", &x, &y, &c);
  if (x < y) {
    left = x;
    x = y;
    y = left;
  }
  left = c;
  right = 300000000;

  if (x == y)
    a = 2 * c;
  else {
    while (left < right) {
      a = (left + right) / 2;
      b = a * c / (a - c);
      if (a * a - b * b == x * x - y * y) {
        break;
      } else if (a * a - b * b < x * x - y * y) {
        left = a + 0.00001;
      } else {
        right = a;
      }
    }
  }
  printf("%lf\n", sqrt(x * x - a * a));

  return (0);
}
