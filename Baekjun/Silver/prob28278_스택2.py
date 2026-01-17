# ---------------------------------------------------------------------------------------------------- #
# https://www.acmicpc.net/problem/28278
# 문제
# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 다섯 가지이다.

# 1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
# 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
# 3: 스택에 들어있는 정수의 개수를 출력한다.
# 4: 스택이 비어있으면 1, 아니면 0을 출력한다.
# 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.

# 입력
# 첫째 줄에 명령의 수 N이 주어진다. (1 ≤ N ≤ 1,000,000)

# 둘째 줄부터 N개 줄에 명령이 하나씩 주어진다.

# 출력을 요구하는 명령은 하나 이상 주어진다.

# 출력
# 출력을 요구하는 명령이 주어질 때마다 명령의 결과를 한 줄에 하나씩 출력한다.
# ---------------------------------------------------------------------------------------------------- #
# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
import sys

input = sys.stdin.readline

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value: int):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop() if len(self.stack) >= 1 else -1

    def size(self):
        return len(self.stack)

    def empty(self):
        return 0 if len(self.stack) >= 1 else 1

    def top(self):
        return self.stack[-1] if len(self.stack) >= 1 else -1

class InstructionError(Exception):
    pass

def main():
    stack = Stack()
    N = int(input())

    for _ in range(N):
        inst = input().split()
        cmd = inst[0]

        if cmd == "1":
            stack.push(int(inst[1]))
        elif cmd == "2":
            # sys.stdout.write(str(stack.pop()))
            print(stack.pop())
        elif cmd == "3":
            # sys.stdout.write(str(stack.size()))
            print(stack.size())
        elif cmd == "4":
            # sys.stdout.write(str(stack.empty()))
            print(stack.empty())
        elif cmd == "5":
            # sys.stdout.write(str(stack.top()))
            print(stack.top())
        else:
            raise InstructionError(f"{inst} is undefined instruction!")

if __name__ == "__main__":
    main()