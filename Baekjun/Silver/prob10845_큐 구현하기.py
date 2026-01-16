# ---------------------------------------------------------------------------------------------------- #
# https://www.acmicpc.net/problem/10845
# 큐

# 문제
# 정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
# 명령은 총 여섯 가지이다.
# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# 입력
# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 
# 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 
# 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

# 출력
# 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
# ---------------------------------------------------------------------------------------------------- #

# https://www.acmicpc.net/blog/view/70 #
# list.pop(0), list.index, list.insert, list.count, x in list, list[:-1] 등은 다 O(N)입니다. 
# 이외에도 O(N)이 걸리는 list 연산이 굉장히 많습니다. https://wiki.python.org/moin/TimeComplexity
# 위의 이유로, list를 큐 또는 덱으로 사용하면 절대, 절대, 절대, 절대, 절대 안 됩니다!! 반드시 collections.deque를 써야 합니다.
# deque 설명: https://velog.io/@harper9808/deque%EB%8A%94-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80

from collections import deque

# main
queue = deque()
Instruction_count = int(input())
output = []
queue_size = 0  # 큐의 크기를 추적하는 변수

for i in range(Instruction_count):
    Instruction = input().split()
    
    if Instruction[0] == "push":
        element = int(Instruction[1])
        queue.append(element)
        queue_size += 1

    elif Instruction[0] == "pop":
        if queue_size:
            output.append(queue.popleft())
            queue_size -= 1
        else:
            output.append(-1)

    elif Instruction[0] == "size":
        output.append(queue_size)

    elif Instruction[0] == "empty":
        output.append(1 if queue_size == 0 else 0)

    elif Instruction[0] == "front":
        if queue_size:
            output.append(queue[0])
        else:
            output.append(-1)

    elif Instruction[0] == "back":
        if queue_size:
            output.append(queue[-1])
        else:
            output.append(-1)

# 한 번에 출력
print("\n".join(map(str, output)))


