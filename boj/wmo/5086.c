#include <stdio.h>

int main() {

    int n, m;
    n = 1;
    m = 1;
    while (n != 0 || m != 0) {
        scanf("%d %d", &n, &m);
        if (n == 0 && m == 0)
            return 0;
    if (n == 0 || m == 0)
        printf("neither\n");
	if (!(n % m))
	    printf("multiple\n");
	else if (!(m % n))
	    printf("factor\n");
	else
	    printf("neither\n");
    }
    return 0;
}
