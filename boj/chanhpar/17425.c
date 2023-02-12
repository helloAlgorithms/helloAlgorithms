#include <stdio.h>

#define MAX 1000000

long fs[MAX + 1];

void
set(void) {
  int i, j;
  for (i = 1; i <= MAX; ++i) {
    for (j = 1; j * i <= MAX; ++j) {
      fs[i * j] += i;
    }
  }
  for (i = 1; i <= MAX; ++i) {
    fs[i] = fs[i] + fs[i - 1];
  }
}

int
main(void) {
  int t, n;
  scanf("%d", &t);
  set();
  while (t-- && scanf("%d", &n))
    printf("%ld\n", fs[n]);
  return (0);
}
