# ---------------------------------------------------------------------------------------------------- #
# https://www.acmicpc.net/problem/10989
# prob10989

# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
# ---------------------------------------------------------------------------------------------------- #

# 풀이 전략
# ---------------------------------------------------------------------------------------------------- #
# 시간 제한 5초, 메모리 제한 8MB
# Python의 sort 내장 함수는 timsort를 사용 -> Time: O(nlogn), Space: O(n)

    # 이 문제에서 Python의 list.sort() / sorted()를 사용할 수 없는 이유 (메모리 관점)
    #
    # - N은 최대 10,000,000 (천만 개)
    # - Python의 int는 객체이므로 정수 하나당 약 28 bytes를 차지함
    #   -> 정수 1천만 개만 저장해도 약 280MB 필요
    #
    # - 리스트는 정수 객체의 포인터 배열이므로
    #   포인터(8 bytes) * 1천만 개 -> 80MB 추가 사용
    #
    # - 즉, 입력을 리스트에 저장하는 순간 메모리 사용량이 300MB 이상이 됨
    # - 또한 Python의 sort(Timsort)는 정렬 과정에서 O(n) 추가 메모리를 사용
    #
    # - 하지만 메모리 제한은 8MB이므로 일반 정렬 방식은 불가능
    # - 수의 범위가 1~10,000으로 매우 작기 때문에 값을 저장하지 않고 개수만 세는 Counting Sort 방식만 가능함
# ---------------------------------------------------------------------------------------------------- #

import sys

# 안정 정렬 구현 버전
"""
def prefix_sum(a: list) -> list:
    for i in range(1, len(a)):
        a[i] += a[i-1]
    return a

def main():
    input = sys.stdin.readline
    N = int(input())

    arr = [0] * N          # 입력 저장
    count = [0] * 10001

    for i in range(N):
        x = int(input())
        arr[i] = x
        count[x] += 1

    prefix_sum(count)      # count[v] = v 이하 개수

    out = [0] * N
    for x in reversed(arr):
        count[x] -= 1
        out[count[x]] = x

    sys.stdout.write("\n".join(map(str, out)) + "\n")
"""

def main():
    input = sys.stdin.readline
    N = int(input())

    # 등장 횟수 저장 -> idx가 해당 값, 리스트에 저장된 값은 등장 횟수
    count = [0] * 10001

    for _ in range(N):
        x = int(input())
        count[x] += 1

    for v in range(0, 10001):
        c = count[v]
        if c:
            for _ in range(c):
                sys.stdout.write(str(v)+"\n")

if __name__ == "__main__":
    main()