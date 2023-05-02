#include <stdio.h>

int arr[8];
int arr1[8] = {1, 2, 3, 4, 5, 6, 7, 8};
int arr2[8] = {8, 7, 6, 5, 4, 3, 2, 1};
int main() {

	int a1, a2;

	a1 = a2 = 1;
	for (int i = 0; i < 8; i++)
		scanf("%d", &arr[i]);
	for (int i = 0; i < 8; i++) {
		if (arr[i] != arr1[i])
			a1 = 0;
		if (arr[i] != arr2[i])
			a2 = 0;
	}
	if (a1 == 1) {
		printf("ascending\n");
		return 0;
	}
	if (a2 == 1) {
		printf("descending\n");
		return 0;
	}
	printf("mixed\n");
	return 0;
}
