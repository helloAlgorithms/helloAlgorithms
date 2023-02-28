//
// Created by Alvin Lee on 2023/02/11.
//
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

int main() {
  int snd[8];
  scanf("%d %d %d %d %d %d %d %d", &snd[0], &snd[1], &snd[2], &snd[3], &snd[4], &snd[5], &snd[6], &snd[7]);
  int cnt = 0;
  for (int i = 0; i < 8; i++) {
	if (snd[i] == i + 1) {
	  cnt++;
	}
  }
  if (cnt == 8) {
	printf("ascending");
  }
  else {
	int cnt = 0;
	for (int i = 7; i >= 0; i--) {
	  if (snd[7 - i] == i + 1) {
		cnt++;
	  }
	}
	if (cnt == 8) {
	  printf("descending");
	}
	else {
	  printf("mixed");
	}
  }
}