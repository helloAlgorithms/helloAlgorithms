#include <stdio.h>

int arr[100001];

void merge_sort(int left, int right) {

	int l, m, t, mid;
	int temp[100001];

	if (left >= right)
		return ;
	mid = (left + right) / 2;
	merge_sort(left, mid);
	merge_sort(mid + 1, right);

	l = t = left;
	m = mid + 1;
	while (l <= mid && m <= right) {
		if (arr[l] < arr[m])
			temp[t++] = arr[l++];
		else
			temp[t++] = arr[m++];
	}
	while (l <= mid)
		temp[t++] = arr[l++];
	while (m <= right)
		temp[t++] = arr[m++];
	while (left <= right) {
		arr[left] = temp[left];
		left++;
	}
}

int binary_search(int target, int start, int end) {
	while (start <= end) {
		int mid = (start + end) / 2;
		if (arr[mid] == target)
			return 1;
		if (target > arr[mid])
			start = mid + 1;
		else
			end = mid - 1;
	}
	return 0;
}

int main() {

	int n, m, num;

	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%d", &arr[i]);
	merge_sort(0, n - 1);
	scanf("%d", &m);
	for (int i = 0; i < m; i++) {
		scanf("%d", &num);
		printf("%d\n", binary_search(num, 0, n - 1));
	}
	return 0;
}
