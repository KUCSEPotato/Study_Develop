# ---------------------------------------------------------------------------------------------------- #
# 구간 합 구하기 5
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	256 MB	104153	48658	35808	44.622%
# 문제
# N×N개의 수가 N×N 크기의 표에 채워져 있다. (x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램을 작성하시오. (x, y)는 x행 y열을 의미한다.

# 예를 들어, N = 4이고, 표가 아래와 같이 채워져 있는 경우를 살펴보자.

# 1	2	3	4
# 2	3	4	5
# 3	4	5	6
# 4	5	6	7
# 여기서 (2, 2)부터 (3, 4)까지 합을 구하면 3+4+5+4+5+6 = 27이고, (4, 4)부터 (4, 4)까지 합을 구하면 7이다.

# 표에 채워져 있는 수와 합을 구하는 연산이 주어졌을 때, 이를 처리하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 표의 크기 N과 합을 구해야 하는 횟수 M이 주어진다. (1 ≤ N ≤ 1024, 1 ≤ M ≤ 100,000) 
# 둘째 줄부터 N개의 줄에는 표에 채워져 있는 수가 1행부터 차례대로 주어진다. 
# 다음 M개의 줄에는 네 개의 정수 x1, y1, x2, y2 가 주어지며, (x1, y1)부터 (x2, y2)의 합을 구해 출력해야 한다. 표에 채워져 있는 수는 1,000보다 작거나 같은 자연수이다. (x1 ≤ x2, y1 ≤ y2)

# 출력
# 총 M줄에 걸쳐 (x1, y1)부터 (x2, y2)까지 합을 구해 출력한다.
# ---------------------------------------------------------------------------------------------------- #
N_MAX = 1024
M_MAX = 100000

class OverRangeError(Exception):
    pass

def range_sum(matrix: list, x1: int, y1: int, x2: int, y2: int) -> int:
    start_row, end_row = x1, x2
    start_col, end_col = y1, y2
    offset = end_col - start_col
    result = 0

    for row_idx, row in enumerate(matrix):
        prefix_sum = 0
        if row_idx <= end_row:
            for col_idx, col in enumerate(row):
                if col_idx+offset <= end_col:
                    prefix_sum += col[offset+col_idx]
        result += prefix_sum
    
    return result


def main():
    N, M = map(int, input().split())
    if not (1 <= N <= N_MAX and 1 <= M <= M_MAX):
        raise OverRangeError(f"N or M is too large (N={N}, M={M})")
    
    if not (1 <= N <= N_MAX and 1 <= M <= M_MAX):
        raise OverRangeError(f"N or M is negative or zero (N={N}, M={M})")
    
    # 행렬 생성
    matrix = []

    for _ in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)

    # 구간 입력
    result = []

    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        result.append(range_sum(matrix=matrix, x1=x1, y1=y1, x2=x2, y2=y2))

    # 출력
    for _, val in enumerate(result):
        print(val)

if __name__ == "__main__":
    main()