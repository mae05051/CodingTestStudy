from itertools import combinations
from functools import reduce

def solution1(clothes):
    clothes_set=set()
    for c in range(len(clothes)):#중복제거
        clothes_set.add(clothes[c][1])
        
    if len(clothes_set)==30:
        answer=2**len(clothes_set)-1 #이항정리
        return answer
    
    clothes_count=dict(zip(clothes_set, [0]*len(clothes_set)))
    for cc in range(len(clothes)):
        clothes_count[clothes[cc][1]]+=1 
    #의상의 종류: 의상의 개수 ex){'eyewear': 1, 'headgear': 2}
    
    answer=sum(clothes_count.values()) #의상을 1개만 입을 때는 전체 옷의 개수
    for a in range(2,len(clothes_count)+1):
        cb=list(combinations(clothes_count.values(), a)) #a개만 뽑은 조합의 리스트
        for s in cb:
            answer+=reduce(lambda x, y: x*y, s) #조합 튜플 안의 원소를 모두 곱한 값
            
    return answer
#처음에는 옷의 개수가 모두 다를때만 1C30+2C30+...+30C30 = n^30 - 1(이항 정리)이 성립한다고 생각을 했음
'''
현수 예를 빌려 다시 생각하고 코드 짜보기
ex) {모자:3개, 상의:2개, 하의:2개}
    = (3c0+3c1) x (2c0+2c1) x (2c0+2c1) -1
    = (1+3) x (1+2) x (1+2) -1
    한 의상은 하나만 쓰거나 안쓰거나임
    다 안쓰는 경우 -1은 해줘야함
'''
from functools import reduce

def solution2(clothes):
    clothes_set=set()
    for c in range(len(clothes)):#중복제거
        clothes_set.add(clothes[c][1])
    
    clothes_count=dict(zip(clothes_set, [1]*len(clothes_set)))#미리 1로 선언 (추후 1 안더함)
    for cc in range(len(clothes)):
        clothes_count[clothes[cc][1]]+=1 
    #의상의 종류: 의상의 개수 ex){'eyewear': 1, 'headgear': 2}
    
    if len(clothes_count)==1:
        answer=list(clothes_count.values())[0] - 1
    else:
        answer=reduce(lambda x, y: x*y, clothes_count.values()) - 1 #각 의상의 개수 +1을 더해서 모두 곱해준 후 -1
    return answer

print(solution2([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution2([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))