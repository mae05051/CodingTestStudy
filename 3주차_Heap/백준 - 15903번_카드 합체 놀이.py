import sys
from heapq import heappop, heappush

card_num,cnt =  map(int,sys.stdin.readline().split())
card = sys.stdin.readline().rstrip()
heap=[int(i) for i in card.split(' ')]
heap.sort()

for i in range(cnt):
    min1=heappop(heap)
    min2=heappop(heap)
    heappush(heap, min1+min2)
    heappush(heap, min1+min2)
    
print(sum(heap))
    