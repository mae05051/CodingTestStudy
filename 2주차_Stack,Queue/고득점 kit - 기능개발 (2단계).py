from collections import deque
import math
'''    
def solution(progresses, speeds):
    progresses=deque(progresses)
    speeds=deque(speeds)
    
    cnt=0
    day=0
    answer=[]
    while progresses:
        if progresses[0] + speeds[0] * day >=100: #완료률 + 속도*지난날짜가 100이 넘으면
            cnt+=1 #완료
            progresses.popleft() #뺴주기
            speeds.popleft() #뺴주기
        else:
            if cnt>0: 
                answer.append(cnt)
                cnt=0
            day+=1
        answer.append(cnt)
    return answer
print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
     '''
def solution(progresses, speeds):
    end_day=[]
    for i,j in zip(progresses,speeds):#미리 걸린 날 list만들기
        end_day.append(math.ceil((100-i)/j))
    cnt = 0
    answer = []
    for i in range(1,len(progresses)):
        if end_day[i] > end_day[cnt]:
            answer.append(i - cnt) #한번에 배포되는 수
            cnt = i
    answer.append(len(progresses)-cnt)
    return answer

        
print(solution([93, 30, 55], [1, 30, 5]))
solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])
# solution([6,2,6,2,5,3], [1,1,1,1,1,1])

