# ---------------------------------------------------------------------------------------------------- #
# https://www.acmicpc.net/problem/1018
# 문제
# 지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 
# 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.

# 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 
# 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

# 보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 
# 당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

# 출력
# 첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.
# ---------------------------------------------------------------------------------------------------- #
N_MAX = 50
M_MAX = 50
N_MIN = 8
M_MIN = 8

class RangeError(Exception):
    pass

def count_num_recoloring(candidate_board: list, start_x: int, start_y: int) -> int:
    """
    idx -> i + j가 짝수면 (0,0)의 색, 아니면 다른 색이어야 한다.
    """

    cnt_w = 0 # 시작이 w
    cnt_b = 0 # 시작이 b

    # count
    for i in range(8):
        for j in range(8):
            color = candidate_board[start_x+i][start_y+j] # 비교할 보드 칸의 색
            expected_w = "W" if (i+j) % 2 == 0 else "B" # W 시작에서 기대되는 색
            expected_b = "B" if (i+j) % 2 == 0 else "W" # B 시작에서 기대되는 색

            if color != expected_w: cnt_w+=1
            if color != expected_b: cnt_b+=1

    return min(cnt_w, cnt_b)

def count_least_num_recoloring(board: list, N, M) -> int:
    least_cnt = 10**9

    # 1) board 자르기
    for x in range(N-7):
        for y in range(M-7):
            # 2) 수정 횟수 구하기
            cnt = count_num_recoloring(candidate_board=board, start_x=x, start_y=y)
            least_cnt = min(cnt, least_cnt)

    return least_cnt

def main():
    N, M = map(int, input().split())
    if not (N_MIN <= N <= N_MAX and M_MIN <= M <= M_MAX):
        raise RangeError(f"N or M is not in the range!")
    
    board = [input().strip() for _ in range(N)]

    res = count_least_num_recoloring(board=board, N=N, M=M)
    print(res)

if __name__ == "__main__":
    main()