#include <stdio.h>
#include <stdlib.h>

static int
less(void const* a, void const* b) {
  int const x = *(int const*)a;
  int const y = *(int const*)b;
  if (x > y)
    return (1);
  if (x < y)
    return (-1);
  return (0);
}

int n, m;
int plus[50];
int minus[50];
int plusCount, minusCount;
int left, leftLast, right, rightLast;
int sum;

void
calcLeft(void) {
  int i;

  if (minusCount > m) {
    i = minusCount % m;
    if (i) {
      left += minus[i - 1];
    }
    while (i + m < minusCount) {
      i += m;
      left += minus[i - 1];
    }
  }
  leftLast = minus[minusCount - 1];
}

void
calcRight(void) {
  int i;

  if (plusCount > m) {
    i = plusCount % m;
    if (i) {
      right += plus[i - 1];
    }
    while (i + m < plusCount) {
      i += m;
      right += plus[i - 1];
    }
  }
  rightLast = plus[plusCount - 1];
}

int
main(void) {
  int i, tmp;
  scanf("%d %d", &n, &m);
  for (i = 0; i < n; ++i) {
    scanf("%d", &tmp);
    if (tmp < 0)
      minus[minusCount++] = -tmp;
    else
      plus[plusCount++] = tmp;
  }
  qsort(plus, plusCount, sizeof(int), less);
  qsort(minus, minusCount, sizeof(int), less);
  calcLeft();
  calcRight();
  sum = 2 * left + 2 * right + leftLast + rightLast
        + (leftLast < rightLast ? leftLast : rightLast);
  printf("%d\n", sum);
  return (0);
}
