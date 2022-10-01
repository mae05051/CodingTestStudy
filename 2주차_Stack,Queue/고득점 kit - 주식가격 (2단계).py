from collections import deque
def solution(prices):
    answer = []
    prices=deque(prices)
    
    while prices:
        duration=0
        p=prices.popleft()
        
        for i in prices:
            duration+=1
            if i<p:
                break
        answer.append(duration)
    
    return answer

print(solution([1, 2, 3, 2, 3]))