#include <stdio.h>

int
findParent(int* const parent, int const a) {
  if (a == parent[a])
    return a;
  parent[a] = findParent(parent, parent[a]);
  return parent[a];
}

int
main(void) {
  int n, m;
  int x, a, b, c, d;
  int parent[1000001];
  scanf("%d %d", &n, &m);
  for (x = 0; x <= n; ++x)
    parent[x] = x;
  while (m-- > 0) {
    scanf("%d %d %d", &x, &a, &b);
    c = findParent(parent, a);
    d = findParent(parent, b);
    if (x == 0)
      parent[c] = d;
    else
      printf(c == d ? "YES\n" : "NO\n");
  }
  return 0;
}
