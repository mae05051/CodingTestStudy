def solution(numbers):
    numbers=list(map(str,numbers))
    numbers.sort(reverse=True, key=lambda x:(x*3))#갓태용
    answer = str(int(''.join(numbers)))
    return answer