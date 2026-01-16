# ---------------------------------------------------------------------------------------------------- #
# https://www.acmicpc.net/problem/1316
"""
문제
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

출력
첫째 줄에 그룹 단어의 개수를 출력한다.
"""

def is_group_word(word):
    seen = set() # 더 이상 연속해서 등장하지 않는 등장한 문자 저장
    prev = "" # 이전 문자 저장

    # 그룹인지 체킹하는 핵심 로직
    for char in word:
        if char != prev:
            if char in seen:
                return False # 이전 문자와 다른데 seen 안에 있다면 그룹 단어가 아님.
            seen.add(char) # 이전 문자와 다른데 seen 안에 없으니 추가한다.
        prev = char

    return True

def main():
    N = int(input())
    group_word_cnt = 0

    for _ in range(N):
        checked_word = input()
        if is_group_word(checked_word):
            group_word_cnt += 1
    
    print(group_word_cnt)

if __name__ == "__main__":
    main()