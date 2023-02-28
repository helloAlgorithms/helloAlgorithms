//
// Created by Alvin Lee on 2023/02/11.
//
#include<stdio.h>

int main() {
  int a[10];
  for (int i = 0; i < 10; i++) {
	scanf("%d", &a[i]);
  }
  int cmp[10];
  for (int i = 0; i < 10; i++) {
	cmp[i] = a[i] % 42;
  }
  int cnt[42] = { 0, };
  for (int i = 0; i < 10; i++) {
	for (int j = 0; j < 42; j++) {
	  if (cmp[i] == j) {
		cnt[j] += 1;
	  }
	}
  }
  int rcnt = 0;
  for (int i = 0; i < 42; i++) {
	if (cnt[i] != 0) {
	  rcnt++;
	}
  }
  printf("%d\n", rcnt);
}