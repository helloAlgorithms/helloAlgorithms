#include <stdio.h>

int n, k;

int
powK(int base, int order) {
  int ret;

  ret = 1;
  while (order-- > 0)
    ret *= base;
  return (ret);
}

char
fract(int s, int r, int c) {
  int l;
  int m;

  if (s == 0)
    return ('0');
  l = powK(n, s - 1);
  m = ((n - k) / 2) * l;
  if (r >= m && c >= m && r < ((n + k) / 2) * l && c < ((n + k) / 2) * l)
    return ('1');
  return (fract(s - 1, r % l, c % l));
}

int
main(void) {
  int s, r1, r2, c1, c2;
  int i, j;
  scanf("%d %d %d %d %d %d %d", &s, &n, &k, &r1, &r2, &c1, &c2);

  for (i = r1; i <= r2; ++i) {
    for (j = c1; j <= c2; ++j) {
      printf("%c", fract(s, i, j));
    }
    printf("\n");
  }

  return (0);
}
