def solution(genres, plays):
    
    pair=[] #(고유번호, 장르, 재생횟수) 튜플 만들기
    for i in range(len(genres)):
        pair.append((i, genres[i], plays[i]))
    #[(0, 'classic', 500), (1, 'pop', 600), (2, 'classic', 150), (3, 'classic', 800), (4, 'pop', 2500)]
    
    genres_sum=dict(zip(list(set(genres)),[0]*len(list(set(genres))))) #중복제거 후 value 0 초기화 {'classic': 0, 'pop': 0}
    for j in pair: #장르별 합계 {'classic': 1450, 'pop': 3100}
        genres_sum[j[1]]+=j[2] 
        
    sorted_genres=sorted(genres_sum,key=lambda x:genres_sum[x], reverse=True) #value기준 sort
    
    sorted_std_dic=dict(zip(sorted_genres,list(range(len(sorted_genres))))) #장르 sort lamda 기준 만들기 {'pop': 0, 'classic': 1}
    pair.sort(key=lambda x:(sorted_std_dic[x[1]],-x[2])) #총 재생수가 많은 장르부터 우선 내림차순, 같은 장르에서 재생수 내림차순

    genres_count=dict(zip(list(set(genres)),[0]*len(list(set(genres)))))# 장르별 2개 초과를 체크하기 위한 count dict, 0으로 초기화 {'classic': 0, 'pop': 0}
    answer=[] #2개만 넘지않게 고유번호 append
    for p in pair:
        if genres_count[p[1]] >= 2: #2개 초과 체크
            continue
        
        genres_count[p[1]]+=1#count dict에 카운트
        answer.append(p[0])#고유번호 append

    return answer

solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])