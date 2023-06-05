#include <stdio.h>

#define MAX 101

/* LCS */

int
max(int a, int b) {
  return a > b ? a : b;
}

int dp[MAX][MAX][MAX];

int
main(void) {
  char s1[MAX];
  char s2[MAX];
  char s3[MAX];
  int i1, i2, i3;

  scanf("%s", s1);
  scanf("%s", s2);
  scanf("%s", s3);

  for (i1 = 0; s1[i1]; ++i1)
    for (i2 = 0; s2[i2]; ++i2)
      for (i3 = 0; s3[i3]; ++i3)
        dp[i1 + 1][i2 + 1][i3 + 1]
            = (s1[i1] == s2[i2] && s2[i2] == s3[i3])
                  ? 1 + dp[i1][i2][i3]
                  : max(dp[i1][i2 + 1][i3 + 1],
                        max(dp[i1 + 1][i2][i3 + 1], dp[i1 + 1][i2 + 1][i3]));
  printf("%d", dp[i1][i2][i3]);

  return 0;
}
