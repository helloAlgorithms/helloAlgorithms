#include <stdio.h>

int
m2(const int a, const int b) {
  return a < b ? a : b;
}

int
m3(const int a, const int b, const int c) {
  return m2(a, m2(b, c));
}

int
m4(const int a, const int b, const int c, const int d) {
  return m2(a, m3(b, c, d));
}

void
solve(int const idx, int n) {
  int a, b, c;
  int prev0, prev1, prev2, curr0, curr1, curr2;
  scanf("%d %d %d", &a, &b, &c);
  prev0 = prev1 = b;
  prev2 = b + m2(c, 0);
  while (--n > 0) {
    scanf("%d %d %d", &a, &b, &c);
    curr0 = a + m2(prev0, prev1);
    curr1 = b + m4(prev0, prev1, prev2, curr0);
    curr2 = c + m3(prev1, prev2, curr1);
    prev0 = curr0;
    prev1 = curr1;
    prev2 = curr2;
  }
  printf("%d. %d\n", idx, curr1);
}

int
main(void) {
  int n, i;
  i = 0;
  while (scanf("%d", &n) && n != 0) {
    solve(++i, n);
  }
  return 0;
}
