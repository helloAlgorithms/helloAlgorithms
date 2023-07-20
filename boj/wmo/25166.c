#include <stdio.h>

int main() {

	int s, m;
	scanf("%d %d", &s, &m);

	int flag = 1023;
	if (flag >= s)
		printf("No thanks\n");
	else if (((s - flag) & m) == (s - flag))
		printf("Thanks\n");
	else
		printf("Impossible\n");
	return 0;
}
