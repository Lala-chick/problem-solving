import sys
import heapq

def sort_cards(cards, N):
    if N == 1:
        return 0

    ans = 0
    heapq.heapify(cards)
    while len(cards) > 1:

        card1 = heapq.heappop(cards)
        card2 = heapq.heappop(cards)
        ans += (card1 + card2)

        heapq.heappush(cards, card1+card2)

    return ans

N = int(sys.stdin.readline().rstrip())
cards = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
cards.sort()

print(sort_cards(cards, N))