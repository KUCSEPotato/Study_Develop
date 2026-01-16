# ---------------------------------------------------------------------------------------------------- #
# https://www.acmicpc.net/problem/2609
# 최대공약수와 최소공배수 

# 문제
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 두 개의 자연수가 주어진다.
# 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

# 출력
# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.
# ---------------------------------------------------------------------------------------------------- #

# gcd(a,b) * lcm(a,b) == ab
# if a mod b == r, then gcd(a,b) == gcd(b,r)

# gcd
def gcd(val1, val2):
    while val2 != 0:
        val1, val2 = val2, val1 % val2
    return val1

# lcm
def lcm (gcd_ab, a, b):
    return a * b // gcd_ab

# main
a, b = map(int, input().split())
gcd_ab = gcd(a, b)
lcm_ab = lcm(gcd_ab, a, b)
print(gcd_ab, lcm_ab, sep='\n')