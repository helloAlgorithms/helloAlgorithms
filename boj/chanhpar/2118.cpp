#include <iostream>

int
main(void) {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  int n, front, rear, currDist, diff, maxDist, totalDist;
  int dist[50001];
  int i;
  std::cin >> n;
  dist[0] = 0;
  for (i = 1; i < n; ++i) {
    std::cin >> dist[i];
    dist[i] += dist[i - 1];
  }
  std::cin >> totalDist;
  totalDist += dist[n - 1];

  maxDist = 0;
  front = 0;
  rear = 1;
  while (rear < n) {
    diff = dist[rear] - dist[front];
    currDist = std::min(diff, totalDist - diff);

    maxDist = std::max(maxDist, currDist);

    if (currDist == diff)
      ++rear;
    else
      ++front;
  }
  std::cout << maxDist;
  return (0);
}
