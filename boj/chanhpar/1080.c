#include <stdio.h>

int n, m;
char matA[51][51];
char matB[51][51];
int matXor[51][51];
int flipCount;
int oneLeft;

void
flip(int row, int col) {
  int i, j;
  ++flipCount;
  for (i = 0; i < 3; ++i) {
    for (j = 0; j < 3; ++j) {
      matXor[row + i][col + j] ^= 1;
      if (matXor[row + i][col + j] == 1)
        ++oneLeft;
      else
        --oneLeft;
    }
  }
}

int
main(void) {
  int i, j;
  scanf("%d %d", &n, &m);
  for (i = 0; i < n; ++i) {
    scanf("%s", matA[i]);
  }
  for (i = 0; i < n; ++i) {
    scanf("%s", matB[i]);
  }

  for (i = 0; i < n; ++i) {
    for (j = 0; j < m; ++j) {
      matXor[i][j] = matA[i][j] != matB[i][j];
      oneLeft += matXor[i][j];
    }
  }

  for (i = 0; i + 2 < n; ++i) {
    for (j = 0; j + 2 < m; ++j) {
      if (matXor[i][j])
        flip(i, j);
    }
  }

  if (oneLeft == 0)
    printf("%d\n", flipCount);
  else
    printf("-1\n");

  return (0);
}
