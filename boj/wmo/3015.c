#include <stdio.h>

typedef long long ll;
typedef struct {
	ll idx;
	ll num;
} St;
St stack[500001];
ll size = 0;
int main() {

	ll n,  num;
	ll result = 0;
	ll flag = 0;
	ll tmp;

	scanf("%lld", &n);
	while (n--) {
		scanf("%lld", &num);
		while (size && num > stack[size - 1].num) {
			size--;
			result++;
		}
		if (size == 0)
			tmp = 0;
		else
			tmp = size - 1;
		if (size && (num == stack[size - 1].num)) {
			result += (size - stack[size - 1].idx);
			stack[size].idx = stack[size - 1].idx;
			stack[size].num = num;
			size++;
			continue;
		}
		if (size)
			result++;
		stack[size].idx = tmp;
		stack[size].num = num;
		size++;
	}
	printf("%lld\n", result);
	return (0);
}
