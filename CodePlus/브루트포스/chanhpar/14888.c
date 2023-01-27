#include <stdio.h>

int
add(int a, int b) {
  return (a + b);
}

int
sub(int a, int b) {
  return (a - b);
}

int
mul(int a, int b) {
  return (a * b);
}

int
div(int a, int b) {
  return (a / b);
}

static int (*fn[4])(int, int) = {add, sub, mul, div};

int n;
int arr[11];
int ops[10];
int init[4];
int maxVal = -2147483648;
int minVal = 2147483647;

int
eval(void) {
  int r;
  int i;

  r = arr[0];
  for (i = 1; i < n; ++i) {
    r = fn[ops[i - 1]](r, arr[i]);
  }
  return (r);
}

void
dfs(int start) {
  int val;
  int i;
  if (start == n - 2) {
    val = eval();
    if (maxVal < val)
      maxVal = val;
    if (minVal > val)
      minVal = val;
    return;
  }

  for (i = 0; i < 4; ++i) {
    if (init[i] > 0) {
      ops[start + 1] = i;
      init[i] -= 1;
      dfs(start + 1);
      init[i] += 1;
    }
  }
}

int
main(void) {
  int i;
  scanf("%d", &n);
  for (i = 0; i < n; ++i)
    scanf("%d", &arr[i]);
  for (i = 0; i < 4; ++i)
    scanf("%d", &init[i]);

  dfs(-1);

  printf("%d\n%d\n", maxVal, minVal);

  return (0);
}
