def solution(arr):
    answer = [] #stack
    for a in arr:
        if len(answer)==0: #처음 요소는 무조건 push
            answer.append(a)
        if answer[-1]!=a: #Top과 다르면 push
            answer.append(a)
    return answer

print(solution([1,1,3,3,0,1,1]))