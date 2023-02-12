#include <stdio.h>

enum {
  E = 15,
  S = 28,
  M = 19
};

int
main(void) {
  int e, s, m, y;
  scanf("%d %d %d", &e, &s, &m);
  y = e;
  while ((y + S - 1) % S + 1 != s)
    y += E;
  while ((y + M - 1) % M + 1 != m)
    y += E * S;
  printf("%d\n", y);
  return (0);
}
