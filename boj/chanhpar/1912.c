#include <stdio.h>

int n;
int arr[100001];
int dp[100001];

/* dp */
int
main(void) {
  int n, i, ans;
  scanf("%d", &n);

  scanf("%d", &arr[0]);
  ans = arr[0];
  dp[0] = arr[0];

  for (i = 1; i < n; ++i) {
    scanf("%d", &arr[i]);
    dp[i] = (dp[i - 1] > 0) ? arr[i] + dp[i - 1] : arr[i];
    if (dp[i] > ans)
      ans = dp[i];
  }
  printf("%d", ans);
  return (0);
}

/* acc sum                          */
/* int                              */
/* main(void) {                     */
/*   int n, i, min, ans;            */
/*   scanf("%d", &n);               */

/*   arr[0] = 0;                    */
/*   scanf("%d", &arr[1]);          */

/*   min = arr[1] < 0 ? arr[1] : 0; */
/*   ans = arr[1];                  */
/*   for (i = 2; i < n + 1; ++i) {  */
/*     scanf("%d", &arr[i]);        */

/*     arr[i] += arr[i - 1];        */
/*     if (ans < arr[i] - min)      */
/*       ans = arr[i] - min;        */
/*     if (arr[i] < min)            */
/*       min = arr[i];              */
/*   }                              */
/*   printf("%d", ans);             */
/*   return (0);                    */
/* }                                */
