#include <stdio.h>

long
myAbs(long a) {
  return (a >= 0 ? a : -a);
}

long
myMod(long a, long b) {
  return (((a % b) + b) % b);
}

/* left <= num - y = q * x <= right */

void
guess(long a, long b, long x, long y) {
  const long left = a - y;
  const long right = b - y;
  long piv;

  if (x == 0 || y < 0 || y >= x) {
    printf("Unknwon Number\n");
    return;
  }
  if (myMod(left, x) == 0) {
    if (right < left + x)
      printf("%ld\n", left + y);
    else
      printf("Unknwon Number\n");
  } else {
    piv = left + (x - myMod(left, x));

    if (right >= piv && right < piv + x)
      printf("%ld\n", piv + y);
    else
      printf("Unknwon Number\n");
  }
}

int
main(void) {
  int a, b, x, y;
  scanf("%d %d", &a, &b);
  if (a > b) {
    x = a;
    a = b;
    b = x;
  }
  scanf("%d %d", &x, &y);
  guess(a, b, myAbs(x), y);
  return (0);
}
