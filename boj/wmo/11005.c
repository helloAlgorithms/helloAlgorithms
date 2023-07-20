#include <stdio.h>

char str[] = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
int base;

void rec(int n, int base)
{
	if (n == 0)
		return ;
	rec(n / base, base);
	printf("%c", str[n % base]);
}

int main() {

	int n;
	scanf("%d %d", &n, &base);

	if (n == 0)
		printf("0");
	else 
		rec(n, base);
	return 0;
}
