#include <stdio.h>
#include <string.h>

char str[7];

int main() {

	int flag;
	int n;
	int num;

	flag = 0;
	scanf("%d", &n);
	while (n--) {
		scanf("%s", str);
		if (!strcmp(str, "add")) {
			scanf("%d", &num);
			flag |= (1 << num);
		}
		else if (!strcmp(str, "check")) {
			scanf("%d", &num);
			if (flag & (1 << num))
				printf("1\n");
			else
				printf("0\n");
		}
		else if (!strcmp(str, "toggle")) {
			scanf("%d", &num);
			flag ^= (1 << num);
		}
		else if (!strcmp(str, "remove")) {
			scanf("%d", &num);
			flag &= ~(1 << num);
		}
		else if (!strcmp(str, "all")) {
			for (int i = 1; i < 21; i++)
				flag |= 1 << i;
		}
		else if (!strcmp(str, "empty"))
			flag = 0;
	}
	return 0;
}
