def solution(answers):
    p1=[1, 2, 3, 4, 5]*len(answers)
    p2=[2, 1, 2, 3, 2, 4, 2, 5]*len(answers)
    p3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*len(answers)
    
    p1_n=0
    p2_n=0
    p3_n=0
    
    for i in range(len(answers)):
        if answers[i]==p1[i]:
            p1_n+=1
        if answers[i]==p2[i]:
            p2_n+=1
        if answers[i]==p3[i]:
            p3_n+=1
        
    p_n = [p1_n,p2_n,p3_n]
    
    people=[]
    if max(p_n)==p_n[0]:
        people.append(1)
    if max(p_n)==p_n[1]:
        people.append(2)
    if max(p_n)==p_n[2]:
        people.append(3)
    
    return people

print(solution([1,3,2,4,2]))