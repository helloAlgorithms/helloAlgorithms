#include <stdio.h>

int n, m;
int arr[2000];
char dp[2000][2000];

int
isPalin(int s, int e) {
  if (dp[s][e] == 0) {
    if (s >= e)
      dp[s][e] = 1;
    else if (arr[s] != arr[e])
      dp[s][e] = 2;
    else
      dp[s][e] = isPalin(s + 1, e - 1);
  }
  return (dp[s][e]);
}

int
main(void) {
  int i;
  int s, e;
  scanf("%d", &n);
  for (i = 0; i < n; ++i)
    scanf("%d", &arr[i]);
  scanf("%d", &m);
  while (m--) {
    scanf("%d %d", &s, &e);
    printf("%d\n", isPalin(s - 1, e - 1) == 1);
  }
  return (0);
}
