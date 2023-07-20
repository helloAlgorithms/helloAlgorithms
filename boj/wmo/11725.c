#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct s_list {
	int num;
	struct s_list *next;
} t_list;

typedef struct s_node {
	int count;
	t_list *head;
	t_list *tail;
} t_node;

int v[100001];
t_node *tree;

void insert_node(int a, int b) {
	t_list *p;

	p = malloc(sizeof(t_list));
	p->num = b;
	p->next = 0;
	if (tree[a].count == 0) {
		tree[a].head = p;
		tree[a].tail = p;
		tree[a].count++;
		return ;
	}
	tree[a].tail->next = p;
	tree[a].tail = p;
	tree[a].count++;
}

void destroy_node(int n) {

	t_list *t;
	t_list *temp;
	for (int i = 0; i <= n; i++) {
		t = tree[i].head;
		temp = t;
		while (t) {
			temp = t;
			t = t->next;
			free(temp);
		}
	}
	free(tree);
}

void dfs(int go, int p) {

	t_list *t;
	if (tree[go].count == 0)
		return ;
	v[go] = p;
	t = tree[go].head;
	while (t) {
		if (!v[t->num])
			dfs(t->num, go);
		t = t->next;
	}
}

int main() {

	int n;
	int a, b;

	scanf("%d", &n);
	tree = malloc(sizeof(t_node) * (n + 1));
	memset(tree, 0, sizeof(t_node) * (n + 1));

	for (int i = 0; i < n - 1; i++) {
		scanf("%d %d", &a, &b);
		insert_node(a, b);
		insert_node(b, a);
	}
	dfs(1, 0);
	for (int i = 2; i <= n; i++)
		printf("%d\n", v[i]);
	destroy_node(n);
	return 0;
}
