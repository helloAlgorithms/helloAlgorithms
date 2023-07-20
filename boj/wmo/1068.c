#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct s_list {
	int v;
	struct s_list *next;
} t_list;

typedef struct s_node {
	t_list *head;
	t_list *tail;
	int count;
} t_node;
int visit[50];
void insert_node(t_node *tree, int par, int c) {
	
	t_list *p;

	p = malloc(sizeof(t_list));
	p->next = 0;
	p->v = c;
	if (tree[par].head == 0) {
		tree[par].head = p;
		tree[par].tail = p;
		tree[par].count++;
		return ;
	}
	tree[par].tail->next = p;
	tree[par].tail = p;
	tree[par].count++;
}

int dfs(t_node *tree, int v) {

	int count = 0;
	int temp = 0;
	t_list *t;

	if (visit[v])
		return 0;
	if (tree[v].count == 0)
		return 1;
	t = tree[v].head;
	while (t) {
		count += dfs(tree, t->v);
		t = t->next;
		if (count == 0 && t == 0)
			return 1;
	}
	return count;
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

	t_node *tree;
	int root;
	int n;
	int num;

	scanf("%d", &n);

	tree = (t_node *)malloc(sizeof(t_node) * n);
	memset(tree, 0, sizeof(t_node) * n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &num);
		if (num == -1) {
			root = i;
			continue;
		}
		insert_node(tree, num, i);
	}
	scanf("%d", &num);
	visit[num] = 1;
	printf("%d\n", dfs(tree, root));
	destroy_node(tree , root);
	
	return 0;
}
