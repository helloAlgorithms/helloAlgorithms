#include <iostream>

bool room[50][50];
bool visit[50][50];

enum {
  EMPTY,
  WALL
};

enum {
  NORTH,
  EAST,
  SOUTH,
  WEST
};

static int const dx[] = {-1, 0, 1, 0};
static int const dy[] = {0, 1, 0, -1};

struct Robot {
  int row, col, dir;
  int n, m;
  int result;

  Robot(const int row, const int col, const int dir)
      : row(row), col(col), dir(dir), result(0) {
  }

  bool
  isInside(const int r, const int c) const {
    return r >= 0 && r < this->n && c >= 0 && c < this->m;
  }

  bool
  isSurroundClean(void) const {
    for (int i = 0; i < 4; ++i) {
      const int next_row = this->row + dx[i];
      const int next_col = this->col + dy[i];
      if (!isInside(next_row, next_col))
        continue;
      if (room[next_row][next_col] == EMPTY && !visit[next_row][next_col])
        return false;
    }
    return true;
  }

  void
  clean(void) {
    if (!visit[this->row][this->col]) {
      visit[this->row][this->col] = true;
      ++this->result;
    }

    if (isSurroundClean()) {
      const int next_row = this->row + dx[(this->dir + 2) % 4];
      const int next_col = this->col + dy[(this->dir + 2) % 4];
      if (!isInside(next_row, next_col) || room[next_row][next_col] != EMPTY)
        return;
      this->row = next_row;
      this->col = next_col;

    } else {
      this->dir = (this->dir + 3) % 4;
      const int next_row = this->row + dx[this->dir];
      const int next_col = this->col + dy[this->dir];
      if (isInside(next_row, next_col) && room[next_row][next_col] == EMPTY
          && !visit[next_row][next_col]) {
        this->row = next_row;
        this->col = next_col;
      }
    }
    this->clean();
  }
};

int
main(void) {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);

  int n, m;
  int r, c, d;

  std::cin >> n >> m;
  std::cin >> r >> c >> d;

  for (int i = 0; i < n; ++i)
    for (int j = 0; j < m; ++j)
      std::cin >> room[i][j];

  Robot robot(r, c, d);

  robot.n = n;
  robot.m = m;

  robot.clean();
  std::cout << robot.result;

  return 0;
}
