#include <stdio.h>
#include <stdlib.h>

int n;
int land[100][100];

int
bfs(int testHeight) {
  static const int dx[4] = {1, 0, -1, 0};
  static const int dy[4] = {0, 1, 0, -1};
  int q[10000];
  int front, rear, curr, nx, ny;
  int i, j, k;
  int count;
  char visit[10000] = {0};

  count = 0;

  front = 0;
  rear = 0;
  for (i = 0; i < n; ++i) {
    for (j = 0; j < n; ++j) {
      if (land[i][j] <= testHeight || visit[100 * i + j])
        continue;

      visit[100 * i + j] = 1;
      q[rear++] = 100 * i + j;
      ++count;
      while (front != rear) {
        curr = q[front++];
        front %= 10000;
        for (k = 0; k < 4; ++k) {
          nx = curr / 100 + dx[k];
          ny = curr % 100 + dy[k];
          if (nx < 0 || nx >= n || ny < 0 || ny >= n || visit[100 * nx + ny]
              || land[nx][ny] <= testHeight)
            continue;
          visit[100 * nx + ny] = 1;
          q[rear++] = 100 * nx + ny;
          rear %= 10000;
        }
      }
      /* bfs end */
    }
  }
  return count;
}

int
main(void) {
  int i, j;
  int countSafeArea, maxSafeArea;

  scanf("%d", &n);
  for (i = 0; i < n; ++i)
    for (j = 0; j < n; ++j)
      scanf("%d", &land[i][j]);
  maxSafeArea = 1;
  for (i = 1; i <= 99; ++i) {
    countSafeArea = bfs(i);
    if (countSafeArea > maxSafeArea)
      maxSafeArea = countSafeArea;
  }
  printf("%d", maxSafeArea);
  return 0;
}
