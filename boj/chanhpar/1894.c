#include <stdio.h>

int main(void) {
  double a, b, c, d, e, f, g, h, x, y;
  while (scanf("%lf %lf %lf %lf %lf %lf %lf %lf", &a, &b, &c, &d, &e, &f, &g, &h) == 8) {
    if (a == e && b == f) { x = c + g - a; y = d + h - b; }
    else if (a == g && b == h) { x = c + e - a; y = d + f - b; }
    else if (c == e && d == f) { x = a + g - c; y = b + h - d; }
    else { x = a + e - c; y = b + f - d; }
    printf("%.3f %.3f\n", x, y);
  }
  return 0;
}
