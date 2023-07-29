#include <math.h>
#include <stdio.h>

#ifndef M_PI
#  define M_PI 3.141592653589793
#endif

int
main(void) {
  double x1, y1, r1, x2, y2, r2, dd, d, a1, a2, t1, t2, s;
  scanf("%lf %lf %lf %lf %lf %lf", &x1, &y1, &r1, &x2, &y2, &r2);
  x1 -= x2;
  y1 -= y2;
  dd = x1 * x1 + y1 * y1;
  if (dd >= (r1 + r2) * (r1 + r2)) {
    s = 0;
  } else if (dd <= (r1 - r2) * (r1 - r2)) {
    s = M_PI * (r1 < r2 ? r1 * r1 : r2 * r2);
  } else {
    d = sqrt(dd);
    a1 = (dd + r1 * r1 - r2 * r2) / (2 * d);
    a2 = (dd + r2 * r2 - r1 * r1) / (2 * d);
    t1 = acos(a1 / r1);
    t2 = acos(a2 / r2);
    s = r1 * r1 * t1 - (r1 * r1 * sin(2 * t1)) / 2 + r2 * r2 * t2
        - (r2 * r2 * sin(2 * t2)) / 2;
  }
  printf("%.3f\n", s);
  return 0;
}
