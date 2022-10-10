def solution(citations):
    citations.sort(reverse=True)
    for idx, n in enumerate(citations):
        if n>=idx+1:#idx+1번째 인용수가 idx+1(인덱스+1)보다 클때
            answer=idx+1
        elif idx == 0 and n == 0: #인용된 논문이 하나도 없을때
            return 0
        else:
            return answer
    return len(citations) #모든 인용수가 논문수보다 많으면