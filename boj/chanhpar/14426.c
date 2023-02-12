#include <stdio.h>

#define SIZE 6000

int s;

unsigned int q[SIZE][3];
unsigned char visit[SIZE][SIZE];

int head;
int tail;

int currScreen;
int currClip;
int currTime;
int nextScreen;
int nextClip;
int nextTime;

void
push(int screen, int clip, int time) {
  q[tail][0] = screen;
  q[tail][1] = clip;
  q[tail][2] = time;
  tail = (tail + 1) % SIZE;
}

void
pop(void) {
  currScreen = q[head][0];
  currClip = q[head][1];
  currTime = q[head][2];
  head = (head + 1) % SIZE;
}

int
copy(void) {
  if (currScreen == 0)
    return (0);
  nextScreen = currScreen;
  nextClip = currScreen;
  nextTime = currTime + 1;
  if (nextScreen == s)
    return (1);
  if (!visit[nextScreen][nextClip]) {
    visit[nextScreen][nextClip] = 1;
    push(nextScreen, nextClip, nextTime);
  }
  return (0);
}

int
paste(void) {
  if (currClip == 0)
    return (0);
  nextScreen = currClip + currScreen;
  nextClip = currClip;
  nextTime = currTime + 1;
  if (nextScreen == s)
    return (1);
  if (nextScreen < SIZE && !visit[nextScreen][nextClip]) {
    visit[nextScreen][nextClip] = 1;
    push(nextScreen, nextClip, nextTime);
  }
  return (0);
}

int delete(void) {
  if (currScreen <= 0)
    return (0);
  nextScreen = currScreen - 1;
  nextClip = currClip;
  nextTime = currTime + 1;
  if (nextScreen == s)
    return (1);
  if (!visit[nextScreen][nextClip]) {
    visit[nextScreen][nextClip] = 1;
    push(nextScreen, nextClip, nextTime);
  }
  return (0);
}

int
main(void) {
  scanf("%d", &s);
  push(1, 0, 0);
  visit[1][0] = 1;
  while (head != tail) {
    pop();
    if (copy() || paste() || delete ())
      break;
  }
  printf("%d\n", nextTime);
  return (0);
}
