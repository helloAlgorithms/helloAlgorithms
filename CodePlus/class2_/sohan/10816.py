import bisect

N = int(input())
n_cards = list(map(int, input().split(' ')))
M = int(input())
m_cards = list(map(int, input().split(' ')))
n_cards.sort()
for mcard in m_cards:
    print(bisect.bisect_right(n_cards, mcard) -bisect.bisect_left(n_cards, mcard), end=' ')
