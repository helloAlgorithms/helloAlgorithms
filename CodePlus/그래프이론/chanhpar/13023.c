#include <stdio.h>

#define MAX 2000

typedef struct list {
  int val;
  struct list* next;
} list;

list* info[MAX];
list nodes[MAX << 1];

list*
getNewNode(void) {
  static int idx = 0;
  return (&nodes[idx++]);
}

void
addFrined(int x, int y) {
  list* node1 = getNewNode();
  node1->val = y;

  list* node2 = getNewNode();
  node2->val = x;

  node1->next = info[x];
  info[x] = node1;

  node2->next = info[y];
  info[y] = node2;
}

int n, m;
unsigned char visit[MAX >> 3];
unsigned char ans;

void
visitOn(int x) {
  visit[x >> 3] |= 1 << (x & 7);
}

void
visitOff(int x) {
  visit[x >> 3] &= ~(1 << (x & 7));
}

void
dfs(int start, int depth) {
  list* curr;
  if (depth >= 5)
    ans = 1;
  if (ans)
    return;

  for (curr = info[start]; curr; curr = curr->next) {
    if (!(visit[(curr->val) >> 3] & (1 << ((curr->val) & 7)))) {
      visitOn(curr->val);
      dfs(curr->val, depth + 1);
      visitOff(curr->val);
    }
  }
}

int
main(void) {
  int i, x, y;
  scanf("%d %d", &n, &m);
  for (i = 0; i < m; ++i) {
    scanf("%d %d", &x, &y);
    addFrined(x, y);
  }
  for (i = 0; i < n; ++i) {
    visitOn(i);
    dfs(i, 1);
    visitOff(i);
  }
  printf("%d\n", ans);
  return (0);
}
