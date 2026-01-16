# ---------------------------------------------------------------------------------------------------- #
# https://www.acmicpc.net/problem/11660
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

# 구간합 행렬 구성
def build_prefix(matrix: list[list[int]]) -> list[list[int]]:
    """
    return -> prefix_matrix
    prefix_matrix[i][j] -> matrix의 (1,1) 에서 (i,j)까지의 합
    """
    n = len(matrix)
    prefix_matrix = [[0] * (n+1) for _ in range(n+1)] # 1-based matrix

    # 구간 합 행렬 구하기
    for i in range(1, n+1):
        row_sum = 0
        for j in range(1, n+1):
            row_sum += matrix[i-1][j-1] # 원본 matrix는 0-based이므로 idx-1 해야함.
            prefix_matrix[i][j] = prefix_matrix[i-1][j] + row_sum
    
    return prefix_matrix

# 구간 합 구하기
def range_sum(prefix_matrix: list, x1: int, y1: int, x2: int, y2: int) -> int:
    """
    구간합은 끝까지의 누적합 - 시작 전까지의 누적합
    x1, y1 까지 포함이므로 1씩 빼줘야한다.
    """
    return prefix_matrix[x2][y2] - prefix_matrix[x1-1][y2] - prefix_matrix[x2][y1-1] + prefix_matrix[x1-1][y1-1]

def main():
    N, M = map(int, input().split())
    if not (1 <= N <= N_MAX):
        raise OverRangeError(f"N out of range: {N}")
    if not (1 <= M <= M_MAX):
        raise OverRangeError(f"M out of range: {M}")

    # 행렬 생성
    matrix = []

    for _ in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)

    # 구간 합 행렬 생성
    prefix = build_prefix(matrix=matrix)

    # 결과 출력
    result = []

    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        result.append(range_sum(prefix, x1, y1, x2, y2))

    for i in range(M):
        print(result[i])
        
if __name__ == "__main__":
    main()