#include <math.h>
#include <stdio.h>

int xa, ya, xb, yb, xc, yc;

double
max(double l1, double l2, double l3) {
  if (l1 < l2)
    l1 = l2;
  if (l1 < l3)
    l1 = l3;
  return (l1);
}

double
min(double l1, double l2, double l3) {
  if (l1 > l2)
    l1 = l2;
  if (l1 > l3)
    l1 = l3;
  return (l1);
}

void
solve(void) {
  double l1, l2, l3;

  l1 = sqrt((double)(xa - xb) * (xa - xb) + (ya - yb) * (ya - yb));
  l2 = sqrt((double)(xb - xc) * (xb - xc) + (yb - yc) * (yb - yc));
  l3 = sqrt((double)(xa - xc) * (xa - xc) + (ya - yc) * (ya - yc));
  printf("%.10f\n", 2 * (max(l1, l2, l3) - min(l1, l2, l3)));
}

int
main(void) {
  scanf("%d %d %d %d %d %d", &xa, &ya, &xb, &yb, &xc, &yc);

  if ((xa - xb) * (ya - yc) - (ya - yb) * (xa - xc) == 0)
    printf("-1.0\n");
  else
    solve();
  return (0);
}
