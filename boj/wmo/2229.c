#include <stdio.h>

#define ABS(x)		( ((x)<0)?-(x):(x) )
#define MAX(a, b)	a > b ? a : b

int arr[1000];
int d[1001];

int main() {

	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%d", &arr[i]);

	d[1] = ABS(arr[1] - arr[0]);
	for (int i = 2; i < n; i++) 
		for (int j = 1; j < i; j++) {
			d[i] = MAX(d[i], ABS(arr[j] - arr[i]) + d[j - 1]);
			d[i] = MAX(d[i], d[i - 1]);
		}
	printf("%d\n", d[n - 1]);
	return 0;
}
