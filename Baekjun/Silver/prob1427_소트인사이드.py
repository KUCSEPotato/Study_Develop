# ---------------------------------------------------------------------------------------------------- #
# https://www.acmicpc.net/problem/1427
# 문제
# 배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

# 입력
# 첫째 줄에 정렬하려고 하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.
# ---------------------------------------------------------------------------------------------------- #
def sort_inside(input_str: str) -> list:
    slice_list = []
    for num in input_str:
        slice_list.append(num)

    slice_list.sort(reverse=True)
    ans = "".join(slice_list)

    print(ans)

def main():
    N = input()
    sort_inside(N)

if __name__ == "__main__":
    main()