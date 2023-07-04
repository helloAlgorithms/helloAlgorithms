#include <stdio.h>
#include <stdlib.h>

int
m(const int a, const int b) {
  return a > b ? a : b;
}

int
f(int* a, int n) {
  int maxDiff, i, minElem;

  minElem = a[0];
  maxDiff = -2000000000;
  for (i = 1; i < n; ++i) {
    if (a[i] - minElem > maxDiff)
      maxDiff = a[i] - minElem;
    if (a[i] < minElem)
      minElem = a[i];
  }

  return maxDiff;
}

int
main(void) {
  int n, k, i, a;
  int* b;
  int* c;
  scanf("%d %d", &n, &k);
  b = malloc(sizeof(int) * n);
  c = malloc(sizeof(int) * n);
  for (i = 0; i < n; ++i) {
    scanf("%d", &a);
    b[n - i - 1] = a + k * (i + 1);
    c[i] = a - k * (i + 1);
  }
  printf("%d", m(f(b, n), f(c, n)));
  return 0;
}

/* max(max(b[r] - b[l]), max(c[r] - c[l])); */
/* 25  14  22  13  4                                    */

/* 27  18  28  21  14 // +, L - R                       */
/* 23  10  16  5   -6 // -, R - L                       */

/* 14 = 22 - 4 - 4 = 28 - 14 = (22 + 6) - (4 + 10)      */
/* -22 = -22 + 4 - 4 = -(22 - 6) + (4 - 10) = (-6) - 16 */

/* 0   1000                                             */

/* 2000    5000                                         */
/* -2000   -3000                                        */

/* a[x] - a[y] + k * (x - y) */
