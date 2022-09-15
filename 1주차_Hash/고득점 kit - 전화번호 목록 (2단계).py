def solution(phone_book):
    phone_book.sort() #사전식 정렬

    for pb in range(len(phone_book)):
        
        if phone_book[pb]==phone_book[-1]:#제일 마지막 요소일 때 -> 끝까지 검사해서 접두어 관계가 없었기 때문에 True
            return True

        #사전식으로 정렬했기 때문에 인덱스 처음부터 두개씩 비교 -> pb번째가 pb+1번째의 접두어가 아니면 그 뒤의 요소들을 검사할 필요가 없음
        if phone_book[pb+1].startswith(phone_book[pb]): 
            return False

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))
print(solution(['11111','12', '1111113124','1111126234762', '90']))