#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

int N;
int visit[102];

typedef struct s_list {
    int v;
    struct s_list *next;
}t_list;

typedef struct {
    t_list *head;
    t_list *tail;
}t_tree;

int tree_dfs(t_tree *tree, int v) {
    int count = 0;
    t_list *t;
 	if (v > N) return 0;
   	if (visit[v]) return 0;
    if (tree[v].head == 0)
        return 1;
    count = 1;
    t = tree[v].head;
    while (t) {
        if (!visit[v]) {
        	visit[v] = 1;
        	count += tree_dfs(tree, t->v);
            visit[v] = 0;
        }
        t = t->next;
    }
    return count;
}

void insert_node(t_tree *tree, int p, int c) {
    t_list *new;
    new = malloc(sizeof(t_list));
    memset(new, 0, sizeof(t_list));
    
    new->v = c;
    if (tree[p].head == 0) {
        tree[p].head = new;
        tree[p].tail = new;
        return ;
    }
    tree[p].tail->next = new;
    tree[p].tail = new;
}

void destroy_list(t_list *t) {

    if (t == 0)
        return ;
    destroy_list(t->next);
    free(t);
}

// wires_rows는 2차원 배열 wires의 행 길이, wires_cols는 2차원 배열 wires의 열 길이입니다.
int solution(int n, int** wires, size_t wires_rows, size_t wires_cols) {
    int answer = 2147483647;
    t_tree *tree;
    N = n;
    
    tree = malloc(sizeof(t_tree) * (n + 1));
	for (int k = 0; k < wires_rows; k++) {
   		memset(tree, 0, sizeof(t_tree) * (n + 1));
        
    	for (int i = 0; i < wires_rows; i++) {
            if (i == k) continue ;
        	insert_node(tree, wires[i][0], wires[i][1]);
        	insert_node(tree, wires[i][1], wires[i][0]);
    	}
        int min = 2147483647;
        int max = -2147483648;
        for (int i = 1; i <= N; i++) {
            int cnt = tree_dfs(tree, i);
            if (cnt == 0) continue;
            memset(visit, 0, sizeof(visit));
            if (cnt > max)
                max = cnt;
            if (cnt < min)
                min = cnt;
        }
        if (max - min < answer)
            answer = max - min;
        for (int i = 1; i <= N; i++) {
            if (tree[i].head != 0)
                destroy_list(tree[i].head);
        }
    }
    free(tree);
    return answer;
}
