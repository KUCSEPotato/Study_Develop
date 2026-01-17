# ---------------------------------------------------------------------------------------------------- #
# https://www.acmicpc.net/problem/11478
# 문제
# 문자열 S가 주어졌을 때, S의 서로 다른 부분 문자열의 개수를 구하는 프로그램을 작성하시오.

# 부분 문자열은 S에서 연속된 일부분을 말하며, 길이가 1보다 크거나 같아야 한다.

# 예를 들어, ababc의 부분 문자열은 a, b, a, b, c, ab, ba, ab, bc, aba, bab, abc, abab, babc, ababc가 있고, 서로 다른것의 개수는 12개이다.

# 입력
# 첫째 줄에 문자열 S가 주어진다. S는 알파벳 소문자로만 이루어져 있고, 길이는 1,000 이하이다.

# 출력
# 첫째 줄에 S의 서로 다른 부분 문자열의 개수를 출력한다.
# ---------------------------------------------------------------------------------------------------- #

def find_substring(string: str) -> set:
    
    len_str = len(string)
    substring_set = set()

    for i in range(len_str):
        for j in range(i+1, len_str+1):
            substring_set.add(string[i:j])

    # print(substring_set)

    return substring_set

def main():
    S = input()
    substring_set = find_substring(string=S)
    print(len(substring_set))

if __name__ == "__main__":
    main()