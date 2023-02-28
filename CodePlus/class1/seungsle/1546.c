//
// Created by Alvin Lee on 2023/02/11.
//
#include<stdio.h>

int main() {
  int N;
  scanf("%d", &N);
  double scr[1000] = {0,};
  for (int i = 0; i < N; i++) {
	scanf("%d", &scr[i]);
  }
  double max = scr[0];
  for (int i = 0; i < N; i++) {
	if (max < scr[i])
	  max = scr[i];
  }
  double fscr[1000] = {0,};
  for (int i = 0; i < N; i++) {
	fscr[i] = (scr[i] / (double)max) * (double)100;
  }
  double wscr = 0;
  for (int i = 0; i < N; i++) {
	wscr += fscr[i];
  }
  printf("%.6f", wscr / (double)N);
}