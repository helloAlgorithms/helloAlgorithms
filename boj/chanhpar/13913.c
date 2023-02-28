#include <stdio.h>

#define SIZE 100001

int n, k;

int prev[SIZE];
char visit[SIZE];

int que[SIZE];
int head;
int tail;

int buff[SIZE];

void
push(int t) {
  que[tail++] = t;
  tail %= SIZE;
}

int
pop(void) {
  int tmp;
  tmp = que[head++];
  head %= SIZE;
  return (tmp);
}

int
func1(int t) {
  return (t - 1);
}

int
func2(int t) {
  return (t + 1);
}

int
func3(int t) {
  return (t << 1);
}

static int (*func[3])(int) = {func1, func2, func3};

void
trace(int t) {
  int idx;
  while (t != -1) {
    buff[idx++] = t;
    t = prev[t];
  }

  printf("%d\n", idx - 1);
  while (idx-- > 0) {
    printf("%d ", buff[idx]);
  }
  printf("\n");
}

int
main(void) {
  int top, next;
  int i;

  scanf("%d %d", &n, &k);

  if (n >= k) {
    printf("%d\n", n - k);
    while (n > k)
      printf("%d ", n--);
    printf("%d\n", k);
    return (0);
  }

  visit[n] = 1;
  prev[n] = -1;
  push(n);

  while (head != tail) {
    top = pop();
    for (i = 0; i < 3; ++i) {
      if (top > k && i > 0)
        continue;
      next = func[i](top);
      if (next < 0 || next >= SIZE || visit[next])
        continue;
      visit[next] = 1;
      prev[next] = top;
      if (next == k) {
        trace(next);
        return (0);
      }
      push(next);
    }
  }
  return (0);
}
