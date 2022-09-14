def solution(phone_book):
    #띄어쓰기 제거, str -> int, sort
    # for st in range(len(phone_book)):
    #     phone_book[st]=int(phone_book[st].replace(' ',''))
    phone_book.sort()
    #print(phone_book)
    #다시 int -> str
    # for it in range(len(phone_book)):
    #     phone_book[it]=str(phone_book[it])
    #print(phone_book)

    for pb in range(len(phone_book)):

        breaker1=''
        breaker2=''

        if phone_book[pb]==phone_book[-1]:
            return True

        if len(phone_book[pb])>=len(phone_book[pb+1]):
            continue

        for s in phone_book[pb+1:]:
            if s.find(phone_book[pb])==0:
                breaker1='breaker1'
                break
            if len(phone_book[pb])>=len(s):
                breaker2='breaker2'
        
        if breaker1=='breaker1':
            return False

        if breaker2=='breaker2':
            continue
        
print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))
print(solution(['11111','12', '1111113124','1111126234762', '90']))