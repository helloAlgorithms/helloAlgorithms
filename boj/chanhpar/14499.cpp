#include <cmath>
#include <iostream>

int n, m;
int board[20][20];

enum {
  EAST = 0,
  WEST = 1,
  NORTH = 2,
  SOUTH = 3
};

enum {
  X = 1,
  Y = 2,
  Z = 3
};

static const int dx[] = {0, 0, -1, 1};
static const int dy[] = {1, -1, 0, 0};

struct Dice {
  int x, y;
  int face[6];
  int orient[3];

  Dice(int x, int y) : x(x), y(y), face() {
    orient[0] = X;
    orient[1] = Y;
    orient[2] = Z;
  }

  int
  sign(int axis) {
    if (axis > 0)
      return (1);
    return (-1);
  }

  int&
  getFace(int axis) {
    return (face[(sign(axis) * orient[abs(axis) - 1] + 6) % 7]);
  }

  void
  printTop(void) {
    std::cout << getFace(Z) << "\n";
  }

  void
  changeState(int move) {
    int tmp;
    switch (move) {
      case (EAST):
        tmp = orient[1];
        orient[1] = -orient[2];
        orient[2] = tmp;
        return;
      case (WEST):
        tmp = orient[1];
        orient[1] = orient[2];
        orient[2] = -tmp;
        return;
      case (NORTH):
        tmp = orient[0];
        orient[0] = orient[2];
        orient[2] = -tmp;
        return;
      case (SOUTH):
        tmp = orient[0];
        orient[0] = -orient[2];
        orient[2] = tmp;
        return;
    }
  }

  void
  updateFace(void) {
    if (board[x][y] == 0) {
      board[x][y] = getFace(-Z);
    } else {
      getFace(-Z) = board[x][y];
      board[x][y] = 0;
    }
  }

  void
  roll(int move) {
    if (isValid(move)) {
      x += dx[move];
      y += dy[move];
      changeState(move);
      updateFace();
      printTop();
    }
  }

  bool
  isValid(int move) {
    int nx = x + dx[move];
    int ny = y + dy[move];

    return (nx >= 0 && nx < n && ny >= 0 && ny < m);
  }
};

int
main(void) {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);

  int x, y, k, cmd;

  std::cin >> n >> m >> x >> y >> k;

  Dice dice(x, y);

  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      std::cin >> board[i][j];
    }
  }

  while (k--) {
    std::cin >> cmd;
    dice.roll(cmd - 1);
  }

  return (0);
}
