import math

def solution(progresses, speeds):
    end_day=[]
    for i,j in zip(progresses,speeds):
        end_day.append(math.ceil((100-i)/j))
    print(end_day)
    
    cnt=1
    answer=[]
    for e in range(1,len(end_day)):
        if end_day[e] <= end_day[e-1]:
            cnt+=1
        else:
            answer.append(cnt)
            cnt=1
        if e == len(end_day)-1:
            answer.append(cnt)
    print(answer)
    return answer
        
# solution([93, 30, 55], [1, 30, 5])
# solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])
solution([6,2,6,2,5,3], [1,1,1,1,1,1])

