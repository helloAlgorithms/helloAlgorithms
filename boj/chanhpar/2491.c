#include <stdio.h>

int main(void) {
  int n, a, b, ci, cd, mi, md;
  scanf("%d", &n);
  ci = cd = mi = md = 1;
  scanf("%d", &b);
  while (--n > 0) {
    scanf("%d", &a);
    ci = a >= b ? ci + 1 : 1;
    cd = a <= b ? cd + 1 : 1;
    mi = mi > ci ? mi : ci;
    md = md > cd ? md : cd;
    b = a;
  }
  printf("%d", mi > md ? mi : md);
  return 0;
}
