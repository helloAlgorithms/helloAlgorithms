#include <stdio.h>

int comb[16][16];

int
nCr(int n, int r) {
  if (r == 0)
    return 1;
  if (n < 2 * r)
    return nCr(n, n - r);
  if (comb[n][r] == 0) {
    comb[n][r] = nCr(n - 1, r - 1) + nCr(n - 1, r);
  }
  return comb[n][r];
}

int
main(void) {
  int n, m, k, a, b;
  scanf("%d %d %d", &n, &m, &k);

  if (k == 0) {
    printf("%d", nCr(n + m - 2, n - 1));
  } else {
    a = (k - 1) / m;
    b = (k - 1) % m;
    printf("%d", nCr(a + b, b) * nCr(n + m - a - b - 2, n - 1 - a));
  }
  return 0;
}
