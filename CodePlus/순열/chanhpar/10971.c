#include <stdio.h>

int n;
int city[10][10];
char visit[10];
int route[11];
int idx;
int ans, cost;

void
dfs(int start) {
  int i;
  for (i = 0; i < n; ++i) {
    if (city[start][i] && visit[i] == 0) {
      visit[i] = 1;
      route[idx++] = i;
      cost += city[start][i];
      if (idx == n + 1 && i == route[0]) {
        ans = (ans < cost) ? ans : cost;
      } else if (cost < ans) {
        dfs(i);
      }
      cost -= city[start][i];
      visit[i] = 0;
      --idx;
    }
  }
}

int
main(void) {
  int i, j;
  scanf("%d", &n);
  for (i = 0; i < n; ++i)
    for (j = 0; j < n; ++j)
      scanf("%d", &city[i][j]);
  ans = 0x7fffffff;
  for (i = 0; i < n; ++i) {
    route[idx++] = i;
    dfs(i);
    --idx;
  }
  printf("%d\n", ans);
  return (0);
}
