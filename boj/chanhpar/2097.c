#include <math.h>
#include <stdio.h>

void
minPeri(int n) {
  int s, t;

  if (n <= 4) {
    printf("4\n");
    return;
  }
  s = (int)sqrt(n);
  t = s;
  while (s * t < n)
    ++t;
  printf("%d\n", 2 * (s + t - 2));
}

int
main(void) {
  int n;
  scanf("%d", &n);
  minPeri(n);
  return (0);
}
