#include <stdio.h>

#define MOD 1000000000

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
  long a, b;
  long ans;
  scanf("%ld %ld", &a, &b);

  ans = fibo(b + 2) - fibo(a + 1);
  printf("%ld\n", (ans + MOD) % MOD);
  return (0);
}
