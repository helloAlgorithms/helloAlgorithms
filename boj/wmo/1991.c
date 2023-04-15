#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct s_tree{
	char data;
	struct s_tree *left;
	struct s_tree *right;
}t_tree;

int n;

void insert_node(t_tree *tree, char p, char l, char r) {
	if (l != '.')
		tree[p].left = &tree[l];
	if (r != '.')
		tree[p].right = &tree[r];
}

void preorder(t_tree *t) {
	if (t == 0)
		return ;
	printf("%c", t->data);
	preorder(t->left);
	preorder(t->right);
}

void inorder(t_tree *t) {
	if (t == 0)
		return ;
	inorder(t->left);
	printf("%c", t->data);
	inorder(t->right);
}

void postorder(t_tree *t) {
	if (t == 0)
		return ;
	postorder(t->left);
	postorder(t->right);
	printf("%c", t->data);
}

void free_data(t_tree *t) {
	if (t == 0)
		return ;
	free_data(t->left);
	free_data(t->right);
	free(t);
}

int main() {

	scanf("%d", &n);
	while (getchar() != '\n');

	t_tree *tree;
	char a, b, c;
	a = b = c = 65;

	tree = malloc(sizeof(t_tree) * 100);
	memset(tree, 0, sizeof(t_tree) * 100);
	for (int i = 65; i < 100; i++) 
		tree[i].data = i;
	while (n--) {
		scanf("\n%c %c %c", &a, &b, &c);
		insert_node(tree, a, b, c);
	}
	preorder(&tree[65]);
	printf("\n");
	inorder(&tree[65]);
	printf("\n");
	postorder(&tree[65]);
	free(tree);
	return 0;
}
