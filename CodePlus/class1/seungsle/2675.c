//
// Created by Alvin Lee on 2023/02/11.
//
#include<stdio.h>
#include<string.h>

int main(){
  int T;
  scanf("%d", &T);
  for(int i = 0; i < T; i++){
	int R;
	scanf("%d", &R);
	char S[20];
	scanf("%s", S);
	int len = strlen(S);
	for(int j = 0; j < len; j++){
	  for(int k = 0; k < R; k++){
		printf("%c", S[j]);
	  }
	}
	printf("\n");
  }
}