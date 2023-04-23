#include <stdio.h>

#define MAX 709

int hexa[MAX];
char isHexa[1000001];

int
hexNum(int n) {
  return (n * ((n << 1) - 1));
}

void
minCount(int n) {
  int min;
  int i;

  min = 5;
  for (i = 1; hexa[i] <= n; ++i) {
    if (min > dp[n - hexa[i]])
      min = dp[n - hexa[i]];
  }
  dp[n] = 1 + min;
}

int
isPossible(int n, int count) {
  int i;
  if (count == 1)
    return (isHexa[n]);

  for (i = MAX - 1; i >= 0; --i) {
    if (hexa[i] <= n) {
      if (isPossible(n - hexa[i], count - 1))
        return (1);
    }
  }
  return (0);
}

int
main(void) {
  int n;
  int i;
  scanf("%d", &n);

  for (i = 1; i < MAX; ++i) {
    hexa[i] = hexNum(i);
    isHexa[hexa[i]] = 1;
  }

  /* dp[11] = 6;     */
  /* dp[26] = 6;     */
  /* dp[130] = 5;    */
  /* dp[146858] = 4; */

  /* for (i = 1; i <= n; ++i) { */
  /*   minCount(i);             */
  /* }                          */

  for (i = 1; i < 6; ++i) {
    if (isPossible(n, i))
      return (printf("%d\n", i), 0);
  }
  return (printf("6\n"), 0);
}
