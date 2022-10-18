def solution(sizes):
    #가로 세로 중 큰 값은 big_lst에 추가
    big_lst=[]
    #가로 세로 중 작은 값은 small_lst에 추가
    small_lst=[]
    for i in sizes:
        big_lst.append(max(i))
        small_lst.append(min(i))
    return max(big_lst)*max(small_lst)