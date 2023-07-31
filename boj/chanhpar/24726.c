#include <stdio.h>

int main(void) {
  double ax, ay, bx, by, cx, cy, gx, gy, s;
  scanf("%lf %lf %lf %lf %lf %lf", &ax, &ay, &bx, &by, &cx, &cy);
  gx = (ax + bx + cx) / 3;
  gy = (ay + by + cy) / 3;
  s = (ax * by + bx * cy + cx * ay - ay * bx - by * cx - cy * ax) / 2;
  s *= 2 * 3.14159265359;
  if (s < 0) s = -s;
  printf("%.6lf %.6lf\n", gy * s, gx * s);
  return 0;
}
