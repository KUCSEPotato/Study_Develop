# AVL tree
## definition
- Self-balancing Binary Search Tree의 일종
    - 트리의 높이를 항상 일정하게 유지하여 search, insert, delete operation에서 O(log n)의 성능을 보장
    - 트리의 균형을 유지하기 위해 Rotation operation을 사용
## 특징
1. **균형 인수 (Height Balance Factor)**
    ```
    각 노드에 대해서 Balance Factor를 아래와 같이 계산합니다.
    Balance Factor = Height of Left Subtree - Height of Right Subtree
    
    균형 인수는 -1, 0, 1 중 하나를 유지해야 합니다.
        0: Height of Left Subtree == Height of Right Subtree
        -1: Height of Left Subtree == Height of Right Subtree + 1
        1: Height of Left Subtree + 1 == Height of Right Subtree
    ```
2. **회전 연산**
    ```
    AVL Tree의 회전 연산은 크게 두 가지로 나눌 수 있고, 그 내부에서도 더 자세히 나눌 수 있습니다.

    1. Single Rotation (단순 회전)
        - 트리가 한 쪽 방향으로만 치우친 경우에 사용.
        - LL회전과 RR회전으로 나뉜다.
    2. Double Rotation (이중 회전)
        - 트리가 두 방향으로 치우친 경우 사용.
        - LR회전과 RL회전으로 나뉜다.
    ```
3. **시간 복잡도**
    ```
    - AVL Tree의 search, insert, delete operation O(log n)의 성능을 보장한다는 것이다.
    - 회전 연산이 추가된다는 점이 있으나, 트리의 높이를 항상 일정하게 유지하기 때문에 성능에서 유리하다.
    ```
## AVL Tree의 장단점
### 장점
```
- 가장 큰 장점은 성능이 보장된다는 점입니다. 
    - O(log n): 항상 균형을 유지하기 때문에 최악의 경우에도 시간 복잡도가 보장됩니다.
- 또한, 트리의 균형이 유지되기 때문에 성능이 저하될 위험이 줄어듭니다.
    - 예시: 한 방향으로만 원소가 삽입되는 경우
```
### 단점
```
- 균형을 유지하기 위해 추가된 연산들로 인해 삽입, 삭제 시 일반적인 BST보다 연산량이 증가
- 삽입/삭제가 빈번한 환경에서는 유지 비용 측면에서 부담이 될 수 있습니다.
```
## 동작 원리
AVL Tree에서 균형이 깨지는 경우는 총 4가지 케이스가 있습니다.
### LL case 
- 왼족 자식이 왼쪽 sub-tree를 가지는 경우
    - 왼쪽 자식 노드가 새로운 루트가 되고, 기존의 루트 노드는 왼쪽 자식 노드의 오른쪽 자식이 된다.
    - 해당 연산을 LL rotation이라 하자. (= 오른쪽으로 회전)

### RR case
- 오른쪽 자식이 오른쪽 sub-tree를 가지는 경우
    - 오른족 자식 노드가 새로운 루트가 되고, 기존의 루트 노드는 오른쪽 자식 노드의 왼쪽 자식이 된다.
    - 해당 연산을 RR rotation이라 하자. (= 왼쪽으로 회전)

### LR case
- 왼쪽 자식이 오른쪽 sub-tree를 가지는 경우
    - 왼쪽 자식의 오른쪽 sub-tree를 왼쪽으로 회전시킨 후 LL rotation 적용
    
### RL case
- 오른쪽 자식이 왼쪽 sub-tree를 가지는 경우
    - 오른쪽 자식의 왼쪽 sub-tree를 오른쪽으로 회전시킨 후 RR rotation 적용

### 회전 연산 정리
| 회전 종류 | 조건 (루트 노드의 BF) | 자식 노드의 BF 조건 | 설명 |
|-----------|----------------------|---------------------|------|
| **LL 회전** | BF ≥ +2 | 왼쪽 자식의 BF ≥ 0 | 왼쪽 자식이 다시 왼쪽으로 치우친 경우. <br>단순 **LL 회전**으로 해결. |
| **RR 회전** | BF ≤ -2 | 오른쪽 자식의 BF ≤ 0 | 오른쪽 자식이 다시 오른쪽으로 치우친 경우. <br>단순 **RR 회전**으로 해결. |
| **LR 회전** | BF ≥ +2 | 왼쪽 자식의 BF < 0 | 왼쪽 자식이 오른쪽으로 치우친 경우. <br>먼저 **RR 회전** 후, **LL 회전**. |
| **RL 회전** | BF ≤ -2 | 오른쪽 자식의 BF > 0 | 오른쪽 자식이 왼쪽으로 치우친 경우. <br>먼저 **LL 회전** 후, **RR 회전**. |