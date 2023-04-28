#include <stdio.h>

int h[100001];
int size = 0;

void swap(int *a, int *b) {
	int temp;
	temp = *a;
	*a = *b;
	*b = temp;
}

void push(int x) {
	h[++size] = x;
	int idx = size;

	while (idx != 1) {
		int par = idx / 2;
		if (h[par] <= h[idx]) break ;
		swap(&h[par], &h[idx]);
		idx = par;
	}
}

void pop() {

	if (size == 0)
		return ;
	if (size == 1) {
		size--;
		h[1] = 0;
		return ;
	}
	h[1] = h[size--];
	int cur = 1;
	while (cur * 2 <= size) {
		int left = cur * 2;
		int right = cur * 2 + 1;
		int min_index = left;
		if (h[left] >= h[right] && right <= size)
			min_index = right;
		else
			min_index = left;
		if (h[cur] <= h[min_index]) break;
		swap(&h[cur], &h[min_index]);
		cur = min_index;
	}
}

int main() {

	int n, num;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &num);
		if (num == 0) {
			printf("%d\n", h[1]);
			pop();
		}
		else
			push(num);
	}
	return 0;
}
