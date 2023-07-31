#include <stdio.h>

int
main(void) {
  int w, h, x, y, p, a, b, c;
  scanf("%d %d %d %d %d", &w, &h, &x, &y, &p);
  c = 0;
  while (p--) {
    scanf("%d %d", &a, &b);
    if ((a - x) * (a - x) + (b - y - h / 2) * (b - y - h / 2) <= ((h * h) / 4)
        || (a - x - w) * (a - x - w) + (b - y - h / 2) * (b - y - h / 2)
               <= ((h * h) / 4)
        || ((x <= a && a <= x + w) && (y <= b && b <= y + h)))
      ++c;
  }
  printf("%d", c);
  return 0;
}
