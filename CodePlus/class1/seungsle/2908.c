//
// Created by Alvin Lee on 2023/02/11.
//
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define BUFFER_SIZE 8

int main(void)
{
  char nums[BUFFER_SIZE];
  char num1[4];
  char num2[4];
  char num1_rev[4];
  char num2_rev[4];
  int int_num1;
  int int_num2;
  int i = 2;
  int j = 0;

  scanf("%[^\n]s", nums);
  strncpy(num1, nums, 4);
  strncpy(num2, &nums[4], 4);
  while (i >= 0 && j <= 2)
  {
	num1_rev[i] = num1[j];
	num2_rev[i] = num2[j];
	j++;
	i--;
  }
  num1_rev[3] = '\0';
  num2_rev[3] = '\0';
  int_num1 = atoi(num1_rev);
  int_num2 = atoi(num2_rev);
  if (int_num1 > int_num2)
	printf("%d\n", int_num1);
  else if (int_num2 > int_num1)
	printf("%d\n", int_num2);
}