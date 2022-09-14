def solution(nums):
    a=len(set(nums)) # 중복제거 리스트 길이
    if a<len(nums)/2: #중복제거 리스트가 nums의 길이 절반보다 작으면 중복제거 리스트 길이만큼이 최댓값
        answer=a
    else: #중복제거 리스트가 nums의 길이 절반보다 크면 N/2마리가 최대값
        answer=len(nums)/2
    return answer
    #피드백: min or max 함수 쓰면 한 줄로 끝남 