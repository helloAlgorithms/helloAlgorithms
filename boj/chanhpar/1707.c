#include <stdio.h>
#include <stdlib.h>

enum {
  EMPTY,
  GROUP1,
  GROUP2
};

struct Node;

typedef struct Edge {
  struct Edge* next;
  struct Node* node;
} Edge;

typedef struct Node {
  int val;
  int group;
  struct Edge* edge;
} Node;

int v, e;
Node* nodes;
Edge* edges;
int edgeIdx;

int flag;

void
connectNode(Node* from, Node* to) {
  Edge* tmp;

  tmp = &edges[edgeIdx++];
  tmp->next = from->edge;
  tmp->node = to;
  from->edge = tmp;
}

void
dfs(Node* ptr, int group) {
  Edge* curr;

  if (flag == 0)
    return;
  ptr->group = group;
  for (curr = ptr->edge; curr != NULL; curr = curr->next) {
    if (curr->node->group == EMPTY)
      dfs(curr->node, (group << 1) % 3);
    else if (curr->node->group == group) {
      flag = 0;
      return;
    }
  }
}

int
isBiPart(void) {
  int i;
  flag = 1;

  for (i = 0; flag && i < v; ++i) {
    if (nodes[i].group == EMPTY)
      dfs(&nodes[i], GROUP1);
  }
  return (flag);
}

void
test(void) {
  int x, y;
  int i;

  scanf("%d %d", &v, &e);
  nodes = malloc(sizeof(Node) * v);
  for (i = 0; i < v; ++i) {
    nodes[i].val = i;
    nodes[i].edge = NULL;
    nodes[i].group = EMPTY;
  }

  edges = malloc(sizeof(Edge) * (e << 1));
  edgeIdx = 0;

  for (i = 0; i < e; ++i) {
    scanf("%d %d", &x, &y);
    connectNode(&nodes[x - 1], &nodes[y - 1]);
    connectNode(&nodes[y - 1], &nodes[x - 1]);
  }

  printf(isBiPart() ? "YES\n" : "NO\n");

  free(nodes);
  free(edges);
}

int
main(void) {
  int t;
  scanf("%d", &t);
  while (t--)
    test();
  return (0);
}
