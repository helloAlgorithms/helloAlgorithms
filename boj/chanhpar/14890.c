#include <stdio.h>
#include <string.h>

int n, l;
int board[100][100];
int aux[100];
int count;

int stack[100];
int size;

void
push(int k) {
  stack[size++] = k;
}

int
pop(void) {
  return (stack[--size]);
}

int
top(void) {
  return (stack[size - 1]);
}

void
checkRow(const int i) {
  int j;
  int k;
  int step;

  size = 0;
  memset(aux, 0, sizeof(int) * n);

  for (j = 0; j < n; ++j) {
    if (size == 0 || (step = board[i][j] - top()) == 0) {
      push(board[i][j]);
      continue;
    }

    if (step == 1) {
      if (size < l || aux[j - l] != 0)
        return;
      size = 0;
      push(board[i][j]);

    } else if (step == -1) {
      size = 0;
      if (j + l > n)
        return;
      for (k = 0; k < l; ++k) {
        if (board[i][j] != board[i][j + k]) {
          return;
        }
        aux[j + k] = 1;
      }
      j += l - 1;
      push(board[i][j]);

    } else {
      return;
    }
  }

  ++count;
}

void
checkCol(const int j) {
  int i;
  int k;
  int step;

  size = 0;
  memset(aux, 0, sizeof(int) * n);

  for (i = 0; i < n; ++i) {
    if (size == 0 || (step = board[i][j] - top()) == 0) {
      push(board[i][j]);
      continue;
    }

    if (step == 1) {
      if (size < l || aux[i - l] != 0)
        return;
      size = 0;
      push(board[i][j]);

    } else if (step == -1) {
      size = 0;
      if (i + l > n)
        return;
      for (k = 0; k < l; ++k) {
        if (board[i][j] != board[i + k][j]) {
          return;
        }
        aux[i + k] = 1;
      }
      i += l - 1;
      push(board[i][j]);

    } else {
      return;
    }
  }

  ++count;
}

int
main(void) {
  int i, j;
  scanf("%d %d", &n, &l);
  for (i = 0; i < n; ++i) {
    for (j = 0; j < n; ++j)
      scanf("%d", &board[i][j]);
    checkRow(i);
  }
  for (j = 0; j < n; ++j)
    checkCol(j);
  printf("%d\n", count);
  return (0);
}
