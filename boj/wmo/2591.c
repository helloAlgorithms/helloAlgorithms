#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char str[100];
int arr[100];
int d[100];
int flag;

void error() {
	printf("0\n");
	exit(0);
}
int check_valid(int a, int b) {
	if (a == 0)
		return 0;
	return ((a * 10 + b) < 35);
}

int main() {

	scanf("%s", str);

	if (str[0] == '0')
		error();

	int len = strlen(str);

	for (int i = 0; i < len; i++) {
		arr[i] = str[i] - 48;
	}
	d[0] = 1;
	if (!check_valid(arr[0], arr[1]) && arr[1] == 0)
		error();
	if (check_valid(arr[0], arr[1])) {
		if (arr[1] == 0)
			d[1] = 1;
		else
			d[1] = d[0] + 1;
	}
	else
		d[1] = d[0];

	for (int i = 2; i < len; i++) {
		if (!check_valid(arr[i - 1], arr[i]) && arr[i] == 0)
			error();
		if (check_valid(arr[i - 1], arr[i])) {
			if (arr[i] == 0)
				d[i] = d[i - 2];
			else
				d[i] = d[i - 1] + d[i - 2];
		}
		else
			d[i] = d[i - 1];
	}
	printf("%d\n", d[len - 1]);
	return 0;
}
