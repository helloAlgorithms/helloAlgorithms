#include <stdio.h>
#include <stdlib.h>

int n, m;

int** groups[4];

/* state:                     */
/* 0 1 2 3                    */
/* 4 5 6 7                    */
/* +4 = l-r flip              */
/* 0 - 1 - 2 - 3 = cw rotate  */
/* 4 - 5 - 6 - 7 = ccw rotate */

int state;

void
op1(void);
void
op2(void);
void
op3(void);
void
op4(void);
void
op5(void);
void
op6(void);

void
op1(void) {
  int** tmp;

  state = state + 6 - 4 * (state / 2);

  tmp = groups[0];
  groups[0] = groups[2];
  groups[2] = tmp;

  tmp = groups[1];
  groups[1] = groups[3];
  groups[3] = tmp;
}

void
op2(void) {
  int** tmp;

  state = (state + 4) % 8;

  tmp = groups[0];
  groups[0] = groups[1];
  groups[1] = tmp;

  tmp = groups[2];
  groups[2] = groups[3];
  groups[3] = tmp;
}

void
op3(void) {
  if (state < 4)
    state = (state + 1) % 4;
  else
    state = (state + 3) % 4 + 4;

  op5();
}

void
op4(void) {
  if (state < 4)
    state = (state + 3) % 4;
  else
    state = (state + 1) % 4 + 4;

  op6();
}

void
op5(void) {
  int** tmp;

  tmp = groups[0];
  groups[0] = groups[2];
  groups[2] = groups[3];
  groups[3] = groups[1];
  groups[1] = tmp;
}

void
op6(void) {
  int** tmp;

  tmp = groups[0];
  groups[0] = groups[1];
  groups[1] = groups[3];
  groups[3] = groups[2];
  groups[2] = tmp;
}

static void (*ops[6])(void) = {op1, op2, op3, op4, op5, op6};

void
print(void) {
  int i, j;

  /* 0 -> i, j;                 */
  /* 2 -> n - 1 - i, m - 1 - j; */
  /* 4 -> i, m - 1 - j;         */
  /* 6 -> n - 1 - i, j;         */

  if (state % 2 == 0) {
    for (i = 0; i < n * 2; ++i) {
      for (j = 0; j < m * 2; ++j) {
        printf("%d ",
               groups[(i / n) * 2 + (j / m)]
                     [state % 4 == 0 ? (i % n) : (n - 1 - i % n)]
                     [state % 6 == 0 ? (j % m) : (m - 1 - j % m)]);
      }
      printf("\n");
    }

    /* 1 -> n - 1 - j, i;         */
    /* 3 -> j, m - 1 - i;         */
    /* 5 -> j, i;                 */
    /* 7 -> n - 1 - j, m - 1 - i; */

  } else {
    for (i = 0; i < m * 2; ++i) {
      for (j = 0; j < n * 2; ++j) {
        printf("%d ",
               groups[(i / m) * 2 + (j / n)]
                     [state % 6 != 1 ? (j % n) : (n - 1 - j % n)]
                     [state % 4 == 1 ? (i % m) : (m - 1 - i % m)]);
      }
      printf("\n");
    }
  }
}

int
main(void) {
  int r;
  int i, j;
  int op;
  scanf("%d %d %d", &n, &m, &r);
  n >>= 1;
  m >>= 1;

  for (i = 0; i < 4; ++i) {
    groups[i] = malloc(sizeof(int*) * n);
    for (j = 0; j < n; ++j) {
      groups[i][j] = malloc(sizeof(int) * m);
    }
  }

  for (i = 0; i < n * 2; ++i) {
    for (j = 0; j < m * 2; ++j) {
      scanf("%d", &groups[(i / n) * 2 + (j / m)][i % n][j % m]);
    }
  }

  for (i = 0; i < r; ++i) {
    scanf("%d", &op);
    ops[op - 1]();
  }

  print();

  return (0);
}
