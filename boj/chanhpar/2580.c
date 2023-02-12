#include <stdio.h>

enum {
  ROW,
  COL,
  SQR
};

int board[9][9];
int stack[81][2];
int bitFlag[3][9];
int count;
int isSolved;

void
print(void) {
  int i, j;
  for (i = 0; i < 9; ++i) {
    for (j = 0; j < 9; ++j) {
      printf("%d ", board[i][j]);
    }
    printf("\n");
  }
}

int
isValid(int row, int col, int k) {
  int flag;
  flag = 1 << k;
  return (!(bitFlag[ROW][row] & flag) && !(bitFlag[COL][col] & flag)
          && !(bitFlag[SQR][3 * (row / 3) + col / 3] & flag));
}

void
flagOn(int row, int col, int k) {
  bitFlag[ROW][row] |= 1 << k;
  bitFlag[COL][col] |= 1 << k;
  bitFlag[SQR][3 * (row / 3) + col / 3] |= 1 << k;
}

void
flagOff(int row, int col, int k) {
  bitFlag[ROW][row] &= ~(1 << k);
  bitFlag[COL][col] &= ~(1 << k);
  bitFlag[SQR][3 * (row / 3) + col / 3] &= ~(1 << k);
}

void
solve(void) {
  int x, y;
  int i;
  if (isSolved)
    return;
  if (count == 0) {
    isSolved = 1;
    print();
    return;
  }

  --count;
  x = stack[count][0];
  y = stack[count][1];
  for (i = 1; i <= 9; ++i) {
    if (isValid(x, y, i)) {
      board[x][y] = i;
      flagOn(x, y, i);
      solve();
      flagOff(x, y, i);
      board[x][y] = 0;
    }
  }
  ++count;
}

int
main(void) {
  int i, j;
  for (i = 0; i < 9; ++i) {
    for (j = 0; j < 9; ++j) {
      scanf("%d", &board[i][j]);
      bitFlag[ROW][i] |= 1 << board[i][j];
      bitFlag[COL][j] |= 1 << board[i][j];
      bitFlag[SQR][3 * (i / 3) + j / 3] |= 1 << board[i][j];
      if (board[i][j] == 0) {
        stack[count][0] = i;
        stack[count][1] = j;
        ++count;
      }
    }
  }
  solve();
  return (0);
}
