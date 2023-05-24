#include <stdio.h>
#include <string.h>

enum {
  EMPTY = '.'
};

char field[12][7];
int combo, isCombo;

static const int dx[] = {1, 0, -1, 0};
static const int dy[] = {0, 1, 0, -1};

int
dfs(int row, int col, char from, char to) {
  int next_row, next_col;
  int count;
  int i;

  field[row][col] = to;
  count = 1;
  for (i = 0; i < 4; ++i) {
    next_row = row + dx[i];
    next_col = col + dy[i];
    if (next_row < 0 || next_row >= 12 || next_col < 0 || next_col > 6)
      continue;
    if (field[next_row][next_col] != from)
      continue;
    count += dfs(next_row, next_col, from, to);
  }
  return count;
}

void
puyo(void) {
  int i, j;
  char orig;

  for (i = 0; i < 12; ++i) {
    for (j = 0; j < 6; ++j) {
      if (field[i][j] == EMPTY)
        continue;
      orig = field[i][j];
      if (dfs(i, j, orig, orig ^ 32) >= 4) {
        dfs(i, j, orig ^ 32, '.');
        isCombo = 1;
      }
    }
  }
}

void
fall(void) {
  int i, j, k;

  for (j = 0; j < 6; ++j) {
    i = 11;
    k = 11;

    while (k >= 0) {
      if (field[k][j] != EMPTY) {
        if (i != k) {
          field[i][j] = field[k][j];
          field[k][j] = EMPTY;
        }
        --i;
      }
      --k;
    }
  }
}

int
main(void) {
  int i;

  for (i = 0; i < 12; ++i) {
    scanf("%s", field[i]);
  }
  combo = 0;
  while (1) {
    isCombo = 0;
    puyo();
    fall();
    if (!isCombo)
      break;
    ++combo;
  }

  printf("%d", combo);

  return 0;
}
