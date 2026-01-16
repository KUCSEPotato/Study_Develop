# ---------------------------------------------------------------------------------------------------- #
# https://www.acmicpc.net/problem/24313
# 문제
# 오늘도 서준이는 점근적 표기 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

# 알고리즘의 소요 시간을 나타내는 O-표기법(빅-오)을 다음과 같이 정의하자.

# O(g(n)) = {f(n) | 모든 n ≥ n0에 대하여 f(n) ≤ c × g(n)인 양의 상수 c와 n0가 존재한다}

# 이 정의는 실제 O-표기법(https://en.wikipedia.org/wiki/Big_O_notation)과 다를 수 있다.

# 함수 f(n) = a1n + a0, 양의 정수 c, n0가 주어질 경우 O(n) 정의를 만족하는지 알아보자.

# 입력
# 첫째 줄에 함수 f(n)을 나타내는 정수 a1, a0가 주어진다. (0 ≤ |ai| ≤ 100)

# 다음 줄에 양의 정수 c가 주어진다. (1 ≤ c ≤ 100)

# 다음 줄에 양의 정수 n0가 주어진다. (1 ≤ n0 ≤ 100)

# 출력
# f(n), c, n0가 O(n) 정의를 만족하면 1, 아니면 0을 출력한다.
# ---------------------------------------------------------------------------------------------------- #
MAX = 100
MIN = 0

class RangeError(Exception):
    pass

# a1n + a0 <= cn -> for all n >= n0, (a1-c)n + a0 <= 0 -> 1차 함수가 1사분면에서 n0보다 큰 n에서 양수값을 지니는가?
# 1) a1 - c 가 음수, 2) (a1-c)n0 + a0 이 0 or 음수 or 1) a1 - c 가 0, 2) a0 <= 0
def find_sol(first_coefficient: int, zero_coefficient: int, c: int, n0: int) -> int:
    if first_coefficient > c: return 0

    if first_coefficient == c: return 1 if zero_coefficient <= 0 else 0
    return 1 if (first_coefficient-c)*n0 + zero_coefficient <= 0 else 0

def main():
    a1, a0 = map(int, input().split())
    c = int(input())
    n0 = int(input())

    # if not (MIN <= a1 <= MAX and MIN <= a0 <= MAX): 
    #    raise RangeError("a1 or a0 is out of range!")

    ans = find_sol(first_coefficient=a1, zero_coefficient=a0, c=c, n0=n0)

    print(ans)

if __name__ == "__main__":
    main()

