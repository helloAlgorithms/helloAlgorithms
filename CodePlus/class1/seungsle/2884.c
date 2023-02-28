//
// Created by Alvin Lee on 2023/02/11.
//
#include<stdio.h>
#include<stdlib.h>

int main(){
  int h, m;
  scanf("%d %d", &h, &m);
  if(m - 45 < 0){
	if(h == 0){
	  h = 23;
	}
	else{
	  h -= 1;
	}
	m = 60 - abs(m - 45);
  }
  else{
	m -= 45;
  }

  printf("%d %d", h, m);
}