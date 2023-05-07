#include <stdio.h>

#define QUE_SIZE 10000;

int
isVisit(char* ptr, int r, int c) {
  const int pos = 100 * r + c;
  return ptr[pos >> 3] & (1 << (pos & 7));
}

void
markVisit(char* ptr, int r, int c) {
  const int pos = 100 * r + c;
  ptr[pos >> 3] |= (1 << (pos & 7));
}

int
main(void) {
  int n, m, k;
  int r, c, idx;
  int size, maxSize;
  int que[10000];
  int front, rear, nx, ny;
  char room[10000] = {0};
  char visit[10000 >> 3] = {0};
  static const int dx[] = {1, 0, -1, 0};
  static const int dy[] = {0, 1, 0, -1};

  scanf("%d %d %d", &n, &m, &k);
  while (k--) {
    scanf("%d %d", &r, &c);
    room[100 * (r - 1) + c - 1] = 1;
  }

  front = 0;
  rear = 0;
  maxSize = 0;
  for (r = 0; r < n; ++r) {
    for (c = 0; c < m; ++c) {
      if (room[100 * r + c] == 0 || isVisit(visit, r, c))
        continue;
      size = 1;
      que[rear] = 100 * r + c;
      rear = (rear + 1) % QUE_SIZE;
      markVisit(visit, r, c);
      while (front != rear) {
        k = que[front];
        front = (front + 1) % QUE_SIZE;
        for (idx = 0; idx < 4; ++idx) {
          nx = k / 100 + dx[idx];
          ny = k % 100 + dy[idx];
          if (nx < 0 || nx >= n || ny < 0 || ny >= m)
            continue;
          if (room[100 * nx + ny] == 0 || isVisit(visit, nx, ny))
            continue;
          ++size;
          que[rear] = 100 * nx + ny;
          rear = (rear + 1) % QUE_SIZE;
          markVisit(visit, nx, ny);
        }
      }
      if (size > maxSize)
        maxSize = size;
    }
  }

  printf("%d\n", maxSize);

  return 0;
}
