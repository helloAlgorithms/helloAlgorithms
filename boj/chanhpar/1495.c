#include <stdio.h>

char visit[51][1001];

void
dfs(int idx,
    int prev,
    int const max,
    int const n,
    int const* vol,
    int* maxVol) {
  if (idx > n)
    return;
  if (visit[idx][prev])
    return;
  visit[idx][prev] = 1;
  if (prev + vol[idx] <= max) {
    if (maxVol[idx] < prev + vol[idx])
      maxVol[idx] = prev + vol[idx];
    dfs(idx + 1, prev + vol[idx], max, n, vol, maxVol);
  }
  if (prev - vol[idx] >= 0) {
    if (maxVol[idx] < prev - vol[idx])
      maxVol[idx] = prev - vol[idx];
    dfs(idx + 1, prev - vol[idx], max, n, vol, maxVol);
  }
}

int
main(void) {
  int n, s, m;
  int vol[51];
  int maxVol[51];
  int i;

  scanf("%d %d %d", &n, &s, &m);
  vol[0] = s;
  maxVol[0] = s;
  for (i = 1; i <= n; ++i) {
    scanf("%d", &vol[i]);
    maxVol[i] = -1;
  }
  dfs(1, s, m, n, vol, maxVol);

  printf("%d", maxVol[n]);
  return 0;
}
