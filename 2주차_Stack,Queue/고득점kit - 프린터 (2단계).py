# from collections import deque
# def solution(priorities, location):
#     priorities_q=deque(priorities)
#     location_q=deque(list(range(len(priorities))))
#     sort_list=[]
#     while priorities_q:
#         for i,v in enumerate(priorities_q):
#             if v == max(priorities_q):
#                 for k in range(i):
#                     priorities_q.append(priorities_q.popleft())
#                     location_q.append(location_q.popleft())
#                 priorities_q.popleft()
#                 sort_list.append(location_q.popleft())     
#         return priorities_q

# a=deque([1,2,4,5])
# print(max(a))

# for idx, v in enumerate(a):
#     print(idx,v)

from collections import deque

def solution(priorities, location): 
    priorities = deque([(v, i) for i, v in enumerate(priorities)])
    max_value = max(priorities)[0]#max value 저장
    
    answer = 0
    while priorities:#다 뺄때까지
        v, i = priorities.popleft()
        while v < max_value:#max value보다 작을때까지 꺼내서 뒤로 넣는다.
            priorities.append((v, i))
            v, i = priorities.popleft()#max값을 꺼내고 
        answer += 1
        if i == location:#location과 인덱스가 같은지 비교해서 미리빼주면 시간절약
            return answer
        else:#아니면 다시 max 갱신
            max_value = max(priorities)[0]
        
    return answer


print(solution([1,1,9,1,2,1], 1))