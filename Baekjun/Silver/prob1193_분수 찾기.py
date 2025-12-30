# ---------------------------------------------------------------------------------------------------- #
# https://www.acmicpc.net/problem/1193
# 분수찾기 

# 문제
# 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
# X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.

# 출력
# 첫째 줄에 분수를 출력한다.
# ---------------------------------------------------------------------------------------------------- #

# 중요한 규칙
# 1. n번째 대각선 시점에서는 총 n(n+1)/2 개의 원소가 있다.
# 2. n번째 대각선에서 -> n이 짝수면 1/n에서 n/1로, n이 홀수면 n/1에서 1/n으로 간다.

# 문제 풀이 전략
# 1. 몇 번째 대각선인지 구한다.
# 2. n번째 대각선에서 몇 번째인지 구한다.

# n(n+1)//2 < X 
def find_diagonal(X:int) -> int:
    n = 1
    while X > n*(n+1)//2:
        n+=1
    return n

def get_fraction(X: int):
    diagonal = find_diagonal(X=X)
    prev = diagonal*(diagonal-1)//2 # 이전 대각선 까지의 원소 개수
    offset = X - prev - 1 # zero-based offset

    if diagonal % 2 == 0:
        # 짝수 대각선: 1/n -> n/1
        child = 1 + offset
        parent = diagonal - offset
    else:
        # 홀수 대각선: n/1 -> 1/n
        child = diagonal - offset
        parent = 1 + offset
    return child, parent

def main():
    X = int(input())
    child, parent = get_fraction(X)
    print(f"{child}/{parent}")

if __name__ == "__main__":
    main()