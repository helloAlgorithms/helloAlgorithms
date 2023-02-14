#include <stdio.h>

static int
myMod(int a, int b) {
  if (a >= 0 || a % b == 0)
    return (a % b);
  if (b > 0)
    return (a % b + b);
  return (a % b - b);
}

static void
convertNeg(int x, int b) {
  int quot, rem;

  if (x >= 0 && x + b < 0) {
    printf("%d", x);
    return;
  }

  rem = myMod(x, b);
  quot = (x - rem) / b;
  convertNeg(quot, b);
  printf("%d", rem);
}

int
main(void) {
  int x;
  scanf("%d", &x);
  convertNeg(x, -2);
  return (0);
}
