#include <stdio.h>
#include <stdlib.h>

typedef struct {
  int* begin;
  int* end;
  int* cap;
} vector;

vector edges[100000];
int numSubtree[100000];
int n;

int
getSize(const vector* const v) {
  return (v->end - v->begin);
}

int
getCap(vector const* const v) {
  return (v->cap - v->begin);
}

void
push_back(vector* v, int k) {
  const int oldSize = getSize(v);
  const int oldCap = getCap(v);
  int* newBegin;
  int newCap;
  int i;

  if (v->begin && oldCap > oldSize) {
    *(v->end++) = k;
  } else {
    newCap = (oldCap + 1) << 1;
    newBegin = malloc(sizeof(int) * newCap);

    for (i = 0; i < oldSize; ++i)
      newBegin[i] = v->begin[i];
    newBegin[i] = k;
    free(v->begin);
    v->begin = newBegin;
    v->end = v->begin + (oldSize + 1);
    v->cap = v->begin + newCap;
  }
}

void
dfs(int root, int parent) {
  vector const* const v = &edges[root];
  int const size = getSize(v);
  int i;

  numSubtree[root] = 1;
  for (i = 0; i < size; ++i) {
    if (v->begin[i] != parent) {
      dfs(v->begin[i], root);
      numSubtree[root] += numSubtree[v->begin[i]];
    }
  }
}

int
main(void) {
  int r, q;
  int u, v;
  int i;
  scanf("%d %d %d", &n, &r, &q);

  for (i = 0; i < n - 1; ++i) {
    scanf("%d %d", &u, &v);
    push_back(&edges[u - 1], v - 1);
    push_back(&edges[v - 1], u - 1);
  }
  dfs(r - 1, -1);
  for (i = 0; i < q; ++i) {
    scanf("%d", &u);
    printf("%d\n", numSubtree[u - 1]);
  }
  return (0);
}
