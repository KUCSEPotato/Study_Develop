from random import randint

# --------------------------------------------------------
# 전역 변수: 찾을 '열쇠' (1~100 사이 무작위 정수)
# --------------------------------------------------------
key = randint(1, 100)


class Box:
    """
    Box 클래스
    - items: 상자 안의 아이템 리스트 (다른 Box 객체 or 숫자 아이템)
    - 50% 확률로 안에 또 다른 Box를 넣고, 항상 숫자 아이템을 하나 넣음
    """

    def __init__(self):
        self.items = []
        if randint(0, 1) == 1:  # 50% 확률로 또 다른 상자 추가
            self.items.append(Box())
        self.items.append(randint(1, 100))  # 무작위 숫자 아이템 추가

    def __iter__(self):
        # for 문에서 Box를 순회할 수 있게 하기 위해 iterator 반환
        return iter(self.items)


# --------------------------------------------------------
# 도우미 함수들
# --------------------------------------------------------
def grab_a_box(pile):
    """
    pile(스택)에서 상자를 하나 꺼내 반환.
    pile이 비어 있으면 None 반환.
    """
    if pile:
        return pile.pop()
    return None


def is_a_box(item):
    """item이 Box 인스턴스인지 여부 확인"""
    return isinstance(item, Box)


def is_the_key(item):
    """item이 '열쇠 값'과 동일한지 여부 확인"""
    return item == key


# --------------------------------------------------------
# 반복문 기반 탐색 (While)
# --------------------------------------------------------
def find_the_key_while(main_box):
    """
    스택을 이용한 반복문 기반 탐색
    - main_box부터 시작해서 상자 속 상자를 열어가며 열쇠를 찾음
    - boxes_opened: 열린 상자의 수
    - items_seen: 확인한 아이템의 수
    """
    pile = [main_box]  # 스택 초기값: main_box
    boxes_opened = 0   # 열어본 상자 개수
    items_seen = 0     # 확인한 아이템 개수

    while pile:
        box = grab_a_box(pile)  # 스택에서 상자 꺼내기
        if box is None:
            continue
        boxes_opened += 1
        for item in box:  # 상자 속 아이템 순회
            items_seen += 1
            if is_a_box(item):
                pile.append(item)  # 상자면 스택에 추가
            elif is_the_key(item):
                print("You found the key!")
                print(f"[while] boxes_opened={boxes_opened}, items_seen={items_seen}")
                return True
    # 모든 상자를 다 열었는데도 못 찾음
    print(f"[while] Not found. boxes_opened={boxes_opened}, items_seen={items_seen}")
    return False


# --------------------------------------------------------
# 재귀 기반 탐색 (DFS)
# --------------------------------------------------------
def find_the_key_recursive(main_box):
    """
    재귀(DFS) 기반 탐색
    - counters: 딕셔너리 형태로 열어본 상자 수와 확인한 아이템 수 누적
    - dfs 함수 내부에서 상자 속을 재귀적으로 탐색
    """
    counters = {"boxes_opened": 0, "items_seen": 0}

    def dfs(box):
        if box is None:
            return False
        counters["boxes_opened"] += 1
        for item in box:
            counters["items_seen"] += 1
            if is_a_box(item):
                if dfs(item):
                    return True
            elif is_the_key(item):
                return True
        return False

    found = dfs(main_box)
    if found:
        print("You found the key!")
    else:
        print("Not found.")
    print(f"[recursive] boxes_opened={counters['boxes_opened']}, items_seen={counters['items_seen']}")
    return found


# --------------------------------------------------------
# (선택) 테스트용: 무조건 key를 심어두기
# --------------------------------------------------------
def plant_key_in_random_leaf(root):
    """
    랜덤하게 하위 상자를 타고 내려가서 열쇠(key)를 심어둠
    - 테스트 시 반드시 key가 존재하게 하여 동작 확인 가능
    """
    cur = root
    while True:
        sub_boxes = [it for it in cur if is_a_box(it)]
        if not sub_boxes or randint(0, 1) == 0:
            for i, it in enumerate(cur.items):
                if not is_a_box(it):
                    cur.items[i] = key
                    return
            cur.items.append(key)
            return
        cur = sub_boxes[randint(0, len(sub_boxes) - 1)]


# --------------------------------------------------------
# 실행 예시
# --------------------------------------------------------
def main():
    main_box = Box()
    # 테스트 안정성을 위해 아래 주석 해제 시 반드시 key가 존재
    # plant_key_in_random_leaf(main_box)

    print("Searching for the key using two methods:")
    print(f"key is {key}")
    find_the_key_while(main_box)
    find_the_key_recursive(main_box)


if __name__ == "__main__":
    main()
