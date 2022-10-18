from itertools import permutations
import math

def is_prime_num(n):#소수인지 확인하는 함수
    for i in range(2, int(math.sqrt(n))+1): # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:
            return False
    return True

def solution(numbers):
    cset=set()
    for i in range(1,len(numbers)+1): #조합개수
        for n in permutations(numbers,i): #모든 조합 구하기
            cset.add(int(''.join(list(n)))) #중복제거
    #----조합 짜는거 현수꺼좀 썻음 ㅎ -----

    prime_lst=[]
    for j in cset:
        if j==0 or j==1:
            continue
        if is_prime_num(j) == True:
            prime_lst.append(j)

    return len(prime_lst)

print(solution("011"))