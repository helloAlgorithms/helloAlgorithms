#include <stdio.h>
#include <stdlib.h>

enum {
  WALL = '#',
  SHEEP = 'o',
  WOLF = 'v',
  EMPTY = '.',
  VISITED = '+'
};

int r, c;

int
bfs(int curr_row, int curr_col, int* curr, char** field) {
  int que[250];
  int front, rear, i;
  int next_row, next_col;
  int outside;

  static const int dx[] = {1, 0, -1, 0};
  static const int dy[] = {0, 1, 0, -1};

  outside = 0;
  front = 0;
  rear = 0;

  if (field[curr_row][curr_col] == SHEEP)
    ++curr[0];
  if (field[curr_row][curr_col] == WOLF)
    ++curr[1];
  field[curr_row][curr_col] = VISITED;
  que[rear++] = 250 * curr_row + curr_col;

  while (front != rear) {
    curr_row = que[front] / 250;
    curr_col = que[front] % 250;
    front = (front + 1) % 250;
    for (i = 0; i < 4; ++i) {
      next_row = curr_row + dx[i];
      next_col = curr_col + dy[i];
      if (next_row < 0 || next_row >= r || next_col < 0 || next_col >= c) {
        outside = 1;
        continue;
      }
      if (field[next_row][next_col] == VISITED
          || field[next_row][next_col] == WALL)
        continue;
      if (field[next_row][next_col] == SHEEP)
        ++curr[0];
      if (field[next_row][next_col] == WOLF)
        ++curr[1];
      field[next_row][next_col] = VISITED;
      que[rear] = 250 * next_row + next_col;
      rear = (rear + 1) % 250;
    }
  }

  return outside;
}

int
main(void) {
  int i, j;
  int total[2], curr[2];
  char** field;
  scanf("%d %d", &r, &c);
  field = malloc(sizeof(char*) * r);
  for (i = 0; i < r; ++i) {
    field[i] = malloc(sizeof(char) * (c + 1));
    scanf("%s", field[i]);
  }

  total[0] = 0;
  total[1] = 0;
  for (i = 0; i < r; ++i) {
    for (j = 0; j < c; ++j) {
      if (field[i][j] == VISITED || field[i][j] == WALL)
        continue;
      curr[0] = 0;
      curr[1] = 0;
      if (bfs(i, j, curr, field) != 0)
        continue;
      if (curr[0] > curr[1])
        total[0] += curr[0];
      else
        total[1] += curr[1];
    }
  }
  printf("%d %d", total[0], total[1]);
  return 0;
}
