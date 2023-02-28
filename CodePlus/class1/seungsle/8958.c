//
// Created by Alvin Lee on 2023/02/11.
//
#include<stdio.h>
#include<string.h>

int main(){
  int n;
  scanf("%d", &n);
  for(int i = 0; i < n; i++){
	char ox[80];
	scanf("%s", ox);
	int len = strlen(ox);
	int cnt = 0;
	int temp = 0;
	for(int j = 0; j < len; j++){
	  if(ox[j] == 'X'){
		continue;
	  }
	  else if(ox[j] == 'O'){
		cnt += 1;
		if(ox[j+1] == 'O'){
		  temp += 1;
		  cnt += temp;
		}
		else{
		  temp = 0;
		}
	  }
	}
	printf("%d\n", cnt);
  }
}