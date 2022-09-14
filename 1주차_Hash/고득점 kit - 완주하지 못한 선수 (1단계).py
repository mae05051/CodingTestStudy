def solution(participant, completion):
    participant2=list(set(participant)) #중복제거 리스트 (딕셔너리를 만들기 위해 사용)

    check_dic=dict(zip(participant2,[0]*len(participant2))) # 모든 participant key에 value 0 넣기 ex){'leo': 0, 'kiki': 0, 'eden': 0}

    for p1 in participant: #참여한 선수면 +1
        check_dic[p1]+=1

    for p2 in completion: #완주한 선수면 -1
        check_dic[p2]-=1

    idx=list(check_dic.values()).index(1) #value가 1인 index 찾기 (완주 못한 participant key를 찾기 위해)
    answer=list(check_dic.keys())[idx]

    return answer
#피드백: collection사용하면 빠름