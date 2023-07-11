#include <stdio.h>

void
repeat(char c, int n) {
  while (n-- > 0)
    printf("%c", c);
}

void
putSeries(int* arr, int n) {
  int i;
  for (i = 0; i < n; ++i)
    repeat(i % 2 ? ' ' : '*', arr[i]);
}

int
main(void) {
  int n, i, j, k;
  int arr[400];
  scanf("%d", &n);

  if (n > 1) {
    repeat('*', 4 * n - 3);
    printf("\n*\n");

    for (i = 0; i < 2 * n - 2; ++i) {
      j = 0;
      k = 0;
      for (j = 0; j < i + 2; ++j)
        arr[k++] = 1;
      arr[k++] = 4 * n - 5 - 2 * i;
      for (j = 0; j < i; ++j)
        arr[k++] = 1;
      putSeries(arr, k);
      printf("\n");
    }

    for (i = 0; i < 2 * n - 1; ++i) {
      j = 0;
      k = 0;
      for (j = 0; j < 2 * n - 2 - i; ++j)
        arr[k++] = 1;
      arr[k++] = 2 * i + 1;
      for (j = 0; j < 2 * n - 2 - i; ++j)
        arr[k++] = 1;
      putSeries(arr, k);
      printf("\n");
    }
  } else
    printf("*\n");
  return 0;
}
