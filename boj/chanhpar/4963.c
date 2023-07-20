#include <stdio.h>

enum {
  SEA = '0',
  LAND = '1'
};

void
bfs(char (*map)[50], int row, int col, const int h, const int w) {
  int que[2601], front, rear, k, c, d, e;
  static const int f[] = {1, 0, -1, 0, 1, 1, -1, -1};
  static const int g[] = {0, 1, 0, -1, 1, -1, 1, -1};
  front = rear = 0;
  map[row][col] = SEA;
  que[rear++] = 51 * row + col;
  while (front != rear) {
    c = que[front++];
    for (k = 0; k < 8; ++k) {
      d = c / 51 + f[k];
      e = c % 51 + g[k];
      if (d < 0 || d >= h || e < 0 || e >= w || map[d][e] == SEA)
        continue;
      map[d][e] = SEA;
      que[rear++] = 51 * d + e;
    }
  }
}

void
testcase(const int w, const int h) {
  char map[50][50];
  int i, j, count;
  for (i = 0; i < h; ++i)
    for (j = 0; j < w; ++j)
      scanf(" %c", &map[i][j]);
  count = 0;
  for (i = 0; i < h; ++i) {
    for (j = 0; j < w; ++j) {
      if (map[i][j] == LAND) {
        ++count;
        bfs(map, i, j, h, w);
      }
    }
  }
  printf("%d\n", count);
}

int
main(void) {
  int w, h;
  while (scanf("%d %d", &w, &h) == 2 && !(w == 0 && h == 0)) {
    testcase(w, h);
  }
  return 0;
}
