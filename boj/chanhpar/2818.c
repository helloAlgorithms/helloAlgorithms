#include <stdio.h>

int dice[6] = {1, 2, 3, 4, 5, 6};

void
rollRight(void) {
  int tmp;

  tmp = dice[0];
  dice[0] = dice[3];
  dice[3] = dice[5];
  dice[5] = dice[2];
  dice[2] = tmp;
}

void
rollLeft(void) {
  int tmp;

  tmp = dice[0];
  dice[0] = dice[2];
  dice[2] = dice[5];
  dice[5] = dice[3];
  dice[3] = tmp;
}

void
rollDown(void) {
  int tmp;

  tmp = dice[0];
  dice[0] = dice[4];
  dice[4] = dice[5];
  dice[5] = dice[1];
  dice[1] = tmp;
}

int
main(void) {
  int r, c;
  int i, j;
  long sum;
  scanf("%d %d", &r, &c);
  sum = 14 * r * (c >> 2);
  c &= 3;
  for (i = 0; i < r; ++i) {
    for (j = 0; j < c; ++j) {
      sum += *dice;
      if (j + 1 < c)
        (i % 2 == 0) ? rollRight() : rollLeft();
      else
        rollDown();
    }
  }
  printf("%ld\n", sum);
  return (0);
}
