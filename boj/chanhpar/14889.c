#include <stdio.h>

int n;
int diff = 0x7fffffff;
int data[20][20];
int isGroup1;
int idx1;

void
dfs(int start) {
  int i, j, sum1, sum2;

  if (idx1 == n / 2) {
    sum1 = 0;
    sum2 = 0;
    for (i = 0; i < n; ++i) {
      for (j = i + 1; j < n; ++j) {
        if ((isGroup1 & (1 << i)) && (isGroup1 & (1 << j)))
          sum1 += data[i][j] + data[j][i];
        if (!(isGroup1 & (1 << i)) && !(isGroup1 & (1 << j)))
          sum2 += data[i][j] + data[j][i];
      }
    }
    if (sum1 - sum2 >= 0 && sum1 - sum2 < diff)
      diff = sum1 - sum2;
    return;
  }

  for (i = start + 1; i < n; ++i) {
    isGroup1 |= 1 << i;
    ++idx1;
    dfs(i);
    isGroup1 &= ~(1 << i);
    --idx1;
  }
}

int
main(void) {
  int i, j;
  scanf("%d", &n);
  for (i = 0; i < n; ++i) {
    for (j = 0; j < n; ++j) {
      scanf("%d", &data[i][j]);
    }
  }
  dfs(-1);
  printf("%d\n", diff);
  return (0);
}
