# ---------------------------------------------------------------------------------------------------- #
# https://www.acmicpc.net/problem/11659
"""
문제
수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

출력
총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.

제한
1 ≤ N ≤ 100,000
1 ≤ M ≤ 100,000
1 ≤ i ≤ j ≤ N
"""

# 아래 처럼 그냥 합을 쓰면 범위가 클 경우 시간 초과
# O(k) + O(k) = O(k)
def slice_sum(num_list: list, range_start: int, range_end: int) -> int:
    return sum(num_list[range_start:range_end])

# 누적합 사용
# O(1) 시간
# https://book.acmicpc.net/algorithm/prefix-sum
def prefix_sum(prefix: list, start: int, end: int) -> int:
    return prefix[end] - prefix[start]

def main():
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))

    if len(num_list) > N:
        print("Wrong num cnt!")
        return 1

    result = list()
    prefix = [0]
    for x in num_list:
        prefix.append(prefix[-1] + x)

    for _ in range(M):
        start, end = map(int, input().split())  
        # result.append(slice_sum(num_list=num_list, range_start=start-1, range_end=end)) # zero_based
        result.append(prefix_sum(prefix=prefix, start=start-1, end=end))

    for _, value in enumerate(result):
        print(value) 

if __name__ == "__main__":
    main()