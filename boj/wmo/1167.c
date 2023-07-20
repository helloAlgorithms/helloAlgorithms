#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct s_list {
	int v;
	int d;
	struct s_list *next;
} t_list;

typedef struct s_node {
	t_list *head;
	t_list *tail;
	int count;
} t_node;

int visit[100001];
int max;
int go;
void insert_node(t_node *tree, int v, int a, int dist) {

	t_list *p;

	p = (t_list *)malloc(sizeof(t_list));
	p->v = a;
	p->d = dist;
	p->next = 0;
	if (tree[v].head == 0) {
		tree[v].head = p;
		tree[v].tail = p;
		tree[v].count++;
		return ;
	}
	tree[v].tail->next = p;
	tree[v].tail = p;
	tree[v].count++;
}

void dfs(t_node *tree, int v, int d) {

	t_list *t;
	int dis = 0;
	if (tree[v].count == 0)
		return ;
	visit[v] = 1;
	t = tree[v].head;
	while (t) {
		if (!visit[t->v]) {
			dfs(tree, t->v, d + t->d);
		}
		t = t->next;
	}
	if (d > max) {
		max = d;
		go = v;
	}
}

void destroy_node(t_node *tree, int n) {

	t_list *t;
	t_list *temp;

	for (int i = 0; i <= n; i++) {
		t = tree[i].head;
		while (t) {
			temp = t;
			t = t->next;
			free(temp);
		}
	}
	free(tree);
}

int main() {

	int n;
	int v, a, dist;
	t_node *tree;
	scanf("%d", &n);

	tree = (t_node *)malloc(sizeof(t_node) * (n + 1));
	memset(tree, 0, sizeof(t_node) * (n + 1));
	while (n--) {
		scanf("%d", &v);
		while (1) {
			scanf("%d", &a);
			if (a == -1)
				break;
			scanf("%d", &dist);
			insert_node(tree, v, a, dist);
			insert_node(tree, a, v, dist);
		}
	}
	dfs(tree, 1, 0);
	memset(&visit[0], 0, sizeof(int) * 10000);
	dfs(tree, go, 0);
	destroy_node(tree, n);
	printf("%d\n", max);
	return 0;
}
