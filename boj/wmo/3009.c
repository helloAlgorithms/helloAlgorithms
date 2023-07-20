#include <stdio.h>

int main() {

	int a1, b1;
	int a2, b2;
	int a3, b3;

	scanf("%d %d", &a1, &b1);
	scanf("%d %d", &a2, &b2);
	scanf("%d %d", &a3, &b3);
	printf("%d %d\n", a1^a2^a3, b1^b2^b3);
	return 0;
}
