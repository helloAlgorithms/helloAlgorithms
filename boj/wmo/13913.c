#include <stdio.h>
#include <string.h>

typedef struct {
	int num;
	int try;
} t_point;

t_point q[10000001];
int d[10000001];
int v[100001];
int go[2] = {1, -1};
int head;
int tail;
int n, k;

void enqueue(t_point num){q[tail++] = num;}
void dequeue(){head++;}

void rec(int num, int start) {

	if (d[num] == -1) {
		printf("%d ", num);
		return ;
	}
	rec(d[num], start);
	printf("%d ", num);
}

void bfs(t_point start) {

	v[start.num] = 1;
	enqueue(start);
	d[start.num] = -1;

	while (head < tail) {
		t_point temp = q[head];
		dequeue();
		if (temp.num == k) {
			printf("%d\n", temp.try);
			rec(d[temp.num], start.num);
			printf("%d\n", temp.num);
		}
		for (int i = 0; i < 3; i++) {
			int new;
			if (i == 2 && new > k) continue;
			else if (i == 2)
				new = temp.num * 2;
			else {
				new = temp.num + go[i];
			}
			if (v[new]) continue;
			v[new] = 1;
			t_point nn = {new, temp.try + 1};
			enqueue(nn);
			d[new] = temp.num;
		}
	}
}

int main() {

	t_point temp;

	scanf("%d %d", &n, &k);
	if (n == k) {
		printf("0\n%d\n", k);
		return 0;
	}
	temp.num = n;
	temp.try = 0;
	bfs(temp);
	return 0;
}
