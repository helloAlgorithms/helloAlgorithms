#include <stdio.h>

#define ABS(x) ((x<0)?(-x):(x))
#define MIN(a, b) a > b ? b : a

int main() {

	int x1, x2, y1, y2, num;

	scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
	int a = x1 - x2;
	int b = y1 - y2;
	num = MIN(x1, y1);
	num = MIN(num, x2);
	num = MIN(num, y2);
	a = ABS(a);
	b = ABS(b);
	a = MIN(a, b);
	printf("%d\n", MIN(a, num));
	return 0;
}
