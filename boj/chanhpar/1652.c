#include <stdio.h>

int
countHori(char room[101][101], int n, int curr) {
  int j, len, count;
  j = 0;
  count = 0;
  while (j < n) {
    while (j < n && room[curr][j] == 'X')
      ++j;
    if (j == n)
      break;
    len = 0;
    while (j < n && room[curr][j] == '.') {
      ++len;
      ++j;
    }
    if (len > 1)
      ++count;
  }
  return (count);
}

int
countVert(char room[101][101], int n, int curr) {
  int j, len, count;
  j = 0;
  count = 0;
  while (j < n) {
    while (j < n && room[j][curr] == 'X')
      ++j;
    if (j == n)
      break;
    len = 0;
    while (j < n && room[j][curr] == '.') {
      ++len;
      ++j;
    }
    if (len > 1)
      ++count;
  }
  return (count);
}

int
main(void) {
  int n, i;
  char room[101][101];
  int hori, vert;
  scanf("%d", &n);
  for (i = 0; i < n; ++i)
    scanf("%s", room[i]);
  hori = 0;
  vert = 0;
  for (i = 0; i < n; ++i) {
    hori += countHori(room, n, i);
    vert += countVert(room, n, i);
  }
  printf("%d %d\n", hori, vert);
  return (0);
}
