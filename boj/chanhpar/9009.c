#include <stdio.h>
#include <string.h>

#define SIZE 45

void
solve(int n, int* fibos) {
  int idx;
  char check[SIZE];

  memset(check, 0, sizeof(char) * SIZE);

  idx = SIZE - 1;
  while (idx > 0 && n) {
    if (fibos[idx] <= n) {
      n -= fibos[idx];
      check[idx] = 1;
    }
    --idx;
  }

  for (idx = 0; idx < SIZE; ++idx) {
    if (check[idx])
      printf("%d ", fibos[idx]);
  }
  printf("\n");
}

int
main(void) {
  int t, n;
  const int fibos[SIZE] = {
      0,         1,         1,        2,        3,        5,         8,
      13,        21,        34,       55,       89,       144,       233,
      377,       610,       987,      1597,     2584,     4181,      6765,
      10946,     17711,     28657,    46368,    75025,    121393,    196418,
      317811,    514229,    832040,   1346269,  2178309,  3524578,   5702887,
      9227465,   14930352,  24157817, 39088169, 63245986, 102334155, 165580141,
      267914296, 433494437, 701408733};

  scanf("%d", &t);
  while (t-- > 0) {
    scanf("%d", &n);
    solve(n, fibos);
  }
  return 0;
}
