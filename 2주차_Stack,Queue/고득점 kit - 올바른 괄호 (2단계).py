def solution(s):
    stack=[] #stack
    for i in s:
        if len(stack)==0: #stack이 비었을때
            if i == "(": #(이면 push
                stack.append(i)
            else: #)이면 에초에 False
                return False
        elif i == ")": #stack이 비지 않았을 때 )는 추가는 하지 않고 pop
            stack.pop()
        else:
            stack.append(i)
            
    if len(stack)==0:
        return True
    else:
        return False