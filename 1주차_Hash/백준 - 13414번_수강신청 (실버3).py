import sys

ps,n = map(int,sys.stdin.readline().split())
id_lst = [sys.stdin.readline().strip() for i in range(n)]

dic={}
for i in id_lst:
    if i in dic: #dict의 in은 avg O(1)
        del dic[i] #있으면 삭제
    dic[i]='' #아무값 넣기 -> 제일 마지막에 넣은 값이 맨 뒤로감

for k in list(dic.keys())[:ps]:
    print(k)
#백준에서는 sys.stdin.readline()를 써야하네.. input() x