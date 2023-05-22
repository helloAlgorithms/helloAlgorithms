#include <stdio.h>
#include <string.h>

typedef struct {
  int v1;
  int v2;
  int weight;
} edge;

int
cmp(const void* a, const void* b) {
  const edge* x = (const edge*)a;
  const edge* y = (const edge*)b;
  return x->weight > y->weight ? 1 : -1;
}

int
findParent(int* const parent, int const a) {
  if (a == parent[a])
    return a;
  parent[a] = findParent(parent, parent[a]);
  return parent[a];
}

int
main(void) {
  int v, e, x, y;
  int i;
  int cost, edgeCount;
  int parent[10001];
  edge edges[100000];

  scanf("%d %d", &v, &e);
  for (i = 0; i <= v; ++i)
    parent[i] = i;
  for (i = 0; i < e; ++i)
    scanf("%d %d %d", &edges[i].v1, &edges[i].v2, &edges[i].weight);
  qsort(edges, e, sizeof(edge), cmp);

  cost = 0;
  edgeCount = 0;
  i = 0;

  while (edgeCount + 1 < v) {
    x = findParent(parent, edges[i].v1);
    y = findParent(parent, edges[i].v2);
    if (x != y) {
      parent[x] = y;
      cost += edges[i].weight;
      ++edgeCount;
    }
    ++i;
  }
  printf("%d", cost);
  return 0;
}
