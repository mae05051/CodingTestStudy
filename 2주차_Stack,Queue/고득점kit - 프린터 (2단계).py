from queue import PriorityQueue
def solution(priorities, location):
    pq=PriorityQueue(maxsize=len(priorities))
    for l, p in enumerate(priorities):
        pq.put((p*(-1), l))
    
    for i in range(len(priorities)):
        #loc=pq.get()[1]
        print(pq.get())
        # if loc == location:
        #     return i+1
        

print(solution([1, 1, 9, 1, 1, 1], 0))