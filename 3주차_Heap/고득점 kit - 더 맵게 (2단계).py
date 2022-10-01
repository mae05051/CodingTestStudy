from heapq import heappop, heappush
def solution(scoville, K):
    answer=0
    scoville.sort()
    
    #제한사항: 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.
    a=scoville[0]
    for i in range(1,len(scoville)):
        a+=2*scoville[i]
        
    if a<K:
        return -1
    else:
        while scoville[0]<K:

            min1=heappop(scoville)
            min2=heappop(scoville)

            new=min1+2*min2
            heappush(scoville, new)
            answer+=1

        return answer