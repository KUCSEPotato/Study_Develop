# ---------------------------------------------------------------------------------------------------- #
# https://www.acmicpc.net/problem/1934
""" 
최소공배수 

문제
두 자연수 A와 B에 대해서, A의 배수이면서 B의 배수인 자연수를 A와 B의 공배수라고 한다. 이런 공배수 중에서 가장 작은 수를 최소공배수라고 한다. 예를 들어, 6과 15의 공배수는 30, 60, 90등이 있으며, 최소 공배수는 30이다.

두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 둘째 줄부터 T개의 줄에 걸쳐서 A와 B가 주어진다. (1 ≤ A, B ≤ 45,000)

출력
첫째 줄부터 T개의 줄에 A와 B의 최소공배수를 입력받은 순서대로 한 줄에 하나씩 출력한다.
"""
# ---------------------------------------------------------------------------------------------------- #

# gcd(a,b) * lcm(a,b) == ab
# if a mod b == r, then gcd(a,b) == gcd(b,r)

def gcd(val1, val2):
    if val1 == 1 or val2 == 1:
        return 1

    while val2 != 0:
        val1, val2 = val2, val1 % val2 # gcd(a,b) = gdc (b, a mod b)
    return val1

def lcm(val1, val2):
    gcd_ab = gcd(val1, val2)
    return val1 * val2 // gcd_ab

def main():
    T = int(input())
    
    for _ in range(T):
        a, b = map(int, input().split())
        lcm_ab = lcm(a, b)
        print(lcm_ab)

if __name__ == "__main__":
    main()
