#include <stdio.h>

#define MOD 1000000007

typedef struct {
  long mat[4];
} Matrix;

Matrix
matProd(Matrix x, Matrix y) {
  return ((Matrix){
      ((x.mat[0] * y.mat[0]) % MOD + (x.mat[1] * y.mat[2]) % MOD) % MOD,
      ((x.mat[0] * y.mat[1]) % MOD + (x.mat[1] * y.mat[3]) % MOD) % MOD,
      ((x.mat[2] * y.mat[0]) % MOD + (x.mat[3] * y.mat[2]) % MOD) % MOD,
      ((x.mat[2] * y.mat[1]) % MOD + (x.mat[3] * y.mat[3]) % MOD) % MOD});
}

Matrix
matPow(Matrix m, long n) {
  Matrix r;

  if (n == 1)
    return (m);

  r = matPow(m, n / 2);
  r = matProd(r, r);

  if (n % 2)
    return (matProd(m, r));
  else
    return (r);
}

long
fibo(long n) {
  if (n == 0)
    return (0);
  return (matPow((Matrix){1, 1, 1, 0}, n).mat[2]);
}

int
main(void) {
  int n;
  scanf("%d", &n);

  printf("%ld\n", fibo(n));
  return (0);
}
