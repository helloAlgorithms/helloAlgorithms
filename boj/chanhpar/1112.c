#include <stdio.h>

int
myMod(int a, int b) {
  if (a >= 0 || a % b == 0)
    return (a % b);
  if (b > 0)
    return (a % b + b);
  return (a % b - b);
}

void
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

void
convertPos(int x, int b) {
  if (x < b) {
    printf("%d", x);
    return;
  }
  convertPos(x / b, b);
  printf("%d", x % b);
}

int
main(void) {
  int x, b;
  scanf("%d %d", &x, &b);
  if (b < 0)
    convertNeg(x, b);
  else if (x >= 0)
    convertPos(x, b);
  else {
    printf("-");
    convertPos(-x, b);
  }
  return (0);
}
