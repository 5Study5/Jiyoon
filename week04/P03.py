# 고능한 풀이
def solution(phone_book):
    
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        # 한 번호를 접두어로 갖는 번호는 해당 번호보다 크기가 크므로 정렬했을 때 뒤에 있음!
        # 즉, 자기 자신 제외한 i +1 부터 검사.
        if phone_book[i+1].startswith(phone_book[i]):
            return False
        
    return True



# 시간 초과
def solution(phone_book):
    answer = True
    
    phone_book.sort()
    
    for i in range(len(phone_book)):
        arr = phone_book.copy()
        arr.remove(phone_book[i])
        
        for k in range(len(arr)):
            if (phone_book[i] == arr[k][:len(phone_book[i])]):
                return False

    return answer