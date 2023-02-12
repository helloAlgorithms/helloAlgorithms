#include <stdio.h>

#define SIZE 10000

char visit[1501][1501];

typedef struct {
  int a;
  int b;
  int c;
} Dole;

Dole que[SIZE];
int head;
int tail;

void
push(Dole elem) {
  que[tail++] = elem;
  tail %= SIZE;
}

Dole
pop(void) {
  Dole tmp;

  tmp = que[head++];
  head %= SIZE;
  return (tmp);
}

void
step(int* x, int* y) {
  int tmp;

  if (*x < *y) {
    tmp = *x;
    *x <<= 1;
    *y -= tmp;
  } else {
    tmp = *y;
    *y <<= 1;
    *x -= tmp;
  }
}

Dole
stepAB(Dole k) {
  step(&k.a, &k.b);
  return (k);
}

Dole
stepBC(Dole k) {
  step(&k.b, &k.c);
  return (k);
}

Dole
stepCA(Dole k) {
  step(&k.c, &k.a);
  return (k);
}

int
cmpAB(Dole k) {
  return (k.a == k.b);
}

int
cmpBC(Dole k) {
  return (k.b == k.c);
}

int
cmpCA(Dole k) {
  return (k.c == k.a);
}

Dole (*func[3])(Dole) = {stepAB, stepBC, stepCA};
int (*cmp[3])(Dole) = {cmpAB, cmpBC, cmpCA};

int
main(void) {
  int a, b, c;
  int i;
  int flag;
  Dole tmp;
  Dole next;
  scanf("%d %d %d", &a, &b, &c);
  if ((a + b + c) % 3 != 0)
    return (printf("0\n"), 0);
  push((Dole){a, b, c});
  visit[a][b] = 1;
  while (head != tail) {
    tmp = pop();
    flag = 1;
    for (i = 0; i < 3; ++i) {
      if (cmp[i](tmp))
        continue;
      flag = 0;
      next = func[i](tmp);
      if (visit[next.a][next.b])
        continue;
      visit[next.a][next.b] = 1;
      push(next);
    }
    if (flag) {
      return (printf("1\n"), 0);
    }
  }
  return (printf("0\n"), 0);
}
