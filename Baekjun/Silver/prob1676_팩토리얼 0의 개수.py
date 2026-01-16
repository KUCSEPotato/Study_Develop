# ---------------------------------------------------------------------------------------------------- #
# https://www.acmicpc.net/problem/1676
# 팩토리얼 0의 개수 

# 문제
# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)

# 출력
# 첫째 줄에 구한 0의 개수를 출력한다.
# ---------------------------------------------------------------------------------------------------- #

def counter_zero(num):
    res = 1 # 팩토리얼 결과 값 저장
    zero_count = 0 # 0의 갯수
    # index = 0

    # print(res) # debug point 1

    if num == 0 or num == 1:
        print("0")
        return
    else:
        while (num >= 1):
            res *= num
            num -= 1
        
        # print(res) # debug point 2

# Logic 1
    while res % 10 == 0:
        zero_count += 1
        res //= 10 # 정수 나눗셈 안하면 런타임 에러 (OverflowError) 발생
    
    print(zero_count)

# main
n = int(input())
counter_zero(n)

# Logic 2 
# convert_int_to_string = str(res)

        # for i in range(len(convert_int_to_string)):

        #     # print(convert_int_to_string[-(i+1)]) # debug point 3

        #     if convert_int_to_string[-(i+1)] == '0':
        #         zero_count += 1
        #     else:
        #         break