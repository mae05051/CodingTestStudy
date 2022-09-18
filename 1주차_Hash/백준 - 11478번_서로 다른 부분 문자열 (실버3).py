import sys

str = sys.stdin.readline().rstrip()
cset=set()
for i in range(len(str)):
    for j in range(i+1,len(str)+1):
        cset.add(str[i:j])#모든 부분 문자열 집합에 더해주기(중복은 추가 안 됨)
print(len(cset))