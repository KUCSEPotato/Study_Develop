# ---------------------------------------------------------------------------------------------------- #
# https://www.acmicpc.net/problem/2447
# 문제
# 재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.

# 크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.

# ***
# * *
# ***
# N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다. 예를 들어 크기 27의 패턴은 예제 출력 1과 같다.

# 입력
# 첫째 줄에 N이 주어진다. N은 3의 거듭제곱이다. 즉 어떤 정수 k에 대해 N=3k이며, 이때 1 ≤ k < 8이다.

# 출력
# 첫째 줄부터 N번째 줄까지 별을 출력한다.
# ---------------------------------------------------------------------------------------------------- #
def build(n:int) -> list:
    """
    build_function -> n*n 별 그림을 문자열 리스트로 반환

    n = 3k일 때:
        위쪽 1/3: prev를 가로로 3번 붙임
        가운데 1/3: prev + 공백(k칸) + prev
        아래쪽 1/3: 위쪽과 동일
    
    build(1) = ["*"]
    """
    if n == 1: return ["*"]

    prev = build(n//3)
    line = []

    for i in prev:
        line.append(i*3)
    for i in prev:
        line.append(i + " "*(n//3) + i)
    for i in prev:
        line.append(i*3)
    
    return line

def recursive_star(n:int) -> None:
    for line in build(n):
        print(line)

def main():
    n = int(input())
    recursive_star(n=n)

    return 0

if __name__ == "__main__":
    main()