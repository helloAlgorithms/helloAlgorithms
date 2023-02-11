//
// Created by Alvin Lee on 2023/02/11.
//
#include <stdio.h>
#include <string.h>
# define BUFFER_SIZE 1000000

void lower(char *str)
{
  int i = 0;
  char ch;
  while (str[i])
  {
	ch = str[i];
	if (str[i] >= 'A' && str[i] <= 'Z')
	  str[i] = ch + 32;
	i++;
  }
}

int main()
{
  char result[BUFFER_SIZE];
  char ch;
  int i = 0;
  int n = 0;
  int tmp = 0;
  int tmp_char = 0;
  int dup = 0;
  int m_cnt[32] = {0,};

  while ((ch = getchar()) != '\n' && BUFFER_SIZE > i)
	result[i++] = ch;
  result[i] = '\0';
  i = 0;
  lower(result);
  while (result[i])
  {
	n = result[i++] - 'a';
	m_cnt[n]++;
  }
  i = 0;
  tmp = 0;
  while (i < 32)
  {
	if (m_cnt[i] >= tmp && m_cnt[i] != 0)
	{
	  tmp = m_cnt[i];
	  tmp_char = i + 'a';
	}
	i++;
  }
  i = 0;
  while (i < 32)
  {
	if (tmp == m_cnt[i])
	  dup++;
	i++;
  }
  if (dup >= 2)
	printf("?\n");
  else
	printf("%c\n", tmp_char - 32);
}