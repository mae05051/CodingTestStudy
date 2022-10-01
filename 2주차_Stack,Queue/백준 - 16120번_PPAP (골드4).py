import sys
str=sys.stdin.readline().strip()

stack=[]
for i in str:
    stack.append(i)
    if stack[-4:]==['P','P','A','P']:#스택 뒷쪽이 PPAP면 P로 바꿈
        for j in range(3): #['P','A','P']뺴줌 pop 3번
            stack.pop()
        
if stack==['P']: #결국 P만 남으면 PPAP문자열
    print("PPAP")
else:
    print('NP')
    
