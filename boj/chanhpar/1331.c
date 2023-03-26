#include <stdio.h>
#include <unistd.h>

unsigned char board[6][6];
char buff[120];

int
dist(int a, int b) {
  return (a > b ? a - b : b - a);
}

int
is(int a, int b, int c, int d) {
  if (a == -1)
    return (1);
  return (((1 << dist(a, c)) | (1 << dist(b, d))) == 6);
}

int
main(void) {
  int i;
  int currX, currY, prevX, prevY, startX, startY;
  int isValid;
  read(0, buff, 109);
  i = 0;
  isValid = 1;
  prevX = -1;
  currX = buff[i++] - 'A';
  currY = buff[i++] - '1';
  ++i;
  board[currX][currY] = 1;
  startX = currX;
  startY = currY;
  while (buff[i]) {
    prevX = currX;
    prevY = currY;
    currX = buff[i++] - 'A';
    currY = buff[i++] - '1';
    ++i;
    if (board[currX][currY] || !is(prevX, prevY, currX, currY)) {
      isValid = 0;
      break;
    }
    board[currX][currY] = 1;
  }
  printf(isValid && is(currX, currY, startX, startY) ? "Valid" : "Invalid");
  return (0);
}
