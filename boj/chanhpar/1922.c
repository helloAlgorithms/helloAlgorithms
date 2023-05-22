#include <stdio.h>
#include <stdlib.h>

typedef struct {
  int v1;
  int v2;
  int weight;
} edge;

int parent[1001];

int
cmp(const void* a, const void* b) {
  return ((const edge*)a)->weight > ((const edge*)b)->weight ? 1 : -1;
}

int
findParent(const int idx) {
  if (parent[idx] == idx)
    return idx;
  parent[idx] = findParent(parent[idx]);
  return parent[idx];
}

int
main(void) {
  int n, m, x, y;
  int cost, connection;
  int i;
  edge edges[100000];

  scanf("%d", &n);
  scanf("%d", &m);
  for (i = 0; i <= n; ++i)
    parent[i] = i;
  for (i = 0; i < m; ++i)
    scanf("%d %d %d", &edges[i].v1, &edges[i].v2, &edges[i].weight);

  qsort(edges, m, sizeof(edge), cmp);

  cost = 0;
  connection = 0;
  i = 0;
  while (connection < n - 1) {
    x = findParent(edges[i].v1);
    y = findParent(edges[i].v2);
    if (x != y) {
      parent[x] = y;
      cost += edges[i].weight;
      ++connection;
    }
    ++i;
  }
  printf("%d", cost);
  return 0;
}
