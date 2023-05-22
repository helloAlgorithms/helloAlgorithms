#include <stdio.h>

#define MAX 1001

int
max(int a, int b) {
  return a > b ? a : b;
}

int
main(void) {
  int idx1, idx2;
  char s1[MAX];
  char s2[MAX];
  int dp[MAX][MAX];
  char* ptr;
  scanf("%s", s1), scanf("%s", s2);

  for (idx1 = 0; s1[idx1]; ++idx1)
    dp[idx1][0] = 0;
  for (idx2 = 0; s2[idx2]; ++idx2)
    dp[0][idx2] = 0;

  for (idx1 = 0; s1[idx1]; ++idx1) {
    for (idx2 = 0; s2[idx2]; ++idx2) {
      if (s1[idx1] == s2[idx2]) {
        dp[idx1 + 1][idx2 + 1] = 1 + dp[idx1][idx2];
      } else {
        dp[idx1 + 1][idx2 + 1] = max(dp[idx1][idx2 + 1], dp[idx1 + 1][idx2]);
      }
    }
  }

  printf("%d\n", dp[idx1][idx2]);

  ptr = &s2[MAX - 1];
  *ptr = '\0';
  while (dp[idx1][idx2] > 0) {
    if (dp[idx1][idx2] == dp[idx1 - 1][idx2])
      --idx1;
    else if (dp[idx1][idx2] == dp[idx1][idx2 - 1])
      --idx2;
    else {
      *--ptr = s1[idx1-- - 1];
      --idx2;
    }
  }
  printf("%s", ptr);
  return 0;
}
