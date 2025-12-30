# Btree implementation in Python
# 참고: https://velog.io/@emplam27/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-B-Tree
# 코드는 gpt를 활용하여 작성함.

# ===============================
# B-Tree (Minimum Degree t)
# - All operations: search / insert / delete
# - Pretty printing: level-order & indented
# ===============================

from collections import deque
from typing import List, Optional

class BTreeNode:
    def __init__(self, t: int, leaf: bool):
        self.t = t                 # minimum degree
        self.leaf = leaf           # is leaf
        self.keys: List[int] = []  # sorted keys
        self.children: List["BTreeNode"] = []  # len = 0 if leaf, else (#keys + 1)

    # helper: find the first index >= key (lower_bound)
    def _find_index(self, key: int) -> int:
        i = 0
        while i < len(self.keys) and key > self.keys[i]:
            i += 1
        return i


class BTree:
    def __init__(self, t: int = 2):
        assert t >= 2, "Minimum degree t must be >= 2"
        self.t = t
        self.root = BTreeNode(t, leaf=True)

    # -----------------------
    # Search
    # -----------------------
    def search(self, key: int) -> Optional[BTreeNode]:
        return self._search(self.root, key)

    def _search(self, node: BTreeNode, key: int) -> Optional[BTreeNode]:
        i = node._find_index(key)
        if i < len(node.keys) and node.keys[i] == key:
            return node
        if node.leaf:
            return None
        return self._search(node.children[i], key)

    # -----------------------
    # Insert
    # -----------------------
    def insert(self, key: int):
        # disallow duplicates (optional policy)
        if self.search(key) is not None:
            return

        r = self.root
        # If root is full, split first
        if len(r.keys) == 2 * self.t - 1:
            s = BTreeNode(self.t, leaf=False)
            s.children.append(r)
            self._split_child(s, 0)
            self.root = s
            self._insert_nonfull(s, key)
        else:
            self._insert_nonfull(r, key)

    def _insert_nonfull(self, node: BTreeNode, key: int):
        i = len(node.keys) - 1
        if node.leaf:
            # insert key into node.keys (sorted)
            node.keys.append(0)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
            return

        # internal node: descend to the correct child
        i = node._find_index(key)
        # if child is full, split it, which will push a key up and create room
        if len(node.children[i].keys) == 2 * self.t - 1:
            self._split_child(node, i)
            # after split, decide which of the two children to go down
            if key > node.keys[i]:
                i += 1
        self._insert_nonfull(node.children[i], key)

    def _split_child(self, parent: BTreeNode, i: int):
        t = self.t
        y = parent.children[i]                  # full child
        z = BTreeNode(t, leaf=y.leaf)           # new right node

        # Move y's last t-1 keys to z
        z.keys = y.keys[t:]                     # indices t .. 2t-2  (len t-1)
        mid_key = y.keys[t - 1]                 # median
        y.keys = y.keys[:t - 1]                 # keep 0 .. t-2

        # Move y's last t children to z (if not leaf)
        if not y.leaf:
            z.children = y.children[t:]         # t .. 2t-1 (len t)
            y.children = y.children[:t]         # keep 0 .. t-1

        # Insert new child/link in parent
        parent.children.insert(i + 1, z)
        parent.keys.insert(i, mid_key)

    # -----------------------
    # Delete
    # -----------------------
    def delete(self, key: int):
        self._delete(self.root, key)
        # If root got emptied and it has a child, make that child the new root
        if len(self.root.keys) == 0 and not self.root.leaf:
            self.root = self.root.children[0]

    def _delete(self, node: BTreeNode, key: int):
        t = self.t
        idx = node._find_index(key)

        # Case A: key is in this node
        if idx < len(node.keys) and node.keys[idx] == key:
            if node.leaf:
                # A1: key in leaf -> remove directly
                node.keys.pop(idx)
                return
            # A2: key in internal node
            left_child = node.children[idx]
            right_child = node.children[idx + 1]

            # A2-1: predecessor child has >= t keys
            if len(left_child.keys) >= t:
                pred = self._get_predecessor(left_child)
                node.keys[idx] = pred
                self._delete(left_child, pred)
            # A2-2: successor child has >= t keys
            elif len(right_child.keys) >= t:
                succ = self._get_successor(right_child)
                node.keys[idx] = succ
                self._delete(right_child, succ)
            else:
                # A2-3: both have t-1 -> merge them with the key
                self._merge(node, idx)
                self._delete(left_child, key)  # left_child is now merged node
            return

        # Case B: key is not in this node (must be in subtree or not present)
        if node.leaf:
            # Not found
            return

        # Determine child idx to descend
        child_idx = idx
        child = node.children[child_idx]

        # Ensure child has at least t keys before descending
        if len(child.keys) == t - 1:
            self._fill(node, child_idx)

            # After fill, child pointer may have changed due to merge
            # If merge happened with next sibling, the child to descend might be at same index,
            # otherwise if it merged with previous sibling, we should move to (child_idx - 1).
            if child_idx > len(node.keys):
                child_idx -= 1
        self._delete(node.children[child_idx], key)

    def _get_predecessor(self, node: BTreeNode) -> int:
        # rightmost key in subtree
        cur = node
        while not cur.leaf:
            cur = cur.children[-1]
        return cur.keys[-1]

    def _get_successor(self, node: BTreeNode) -> int:
        # leftmost key in subtree
        cur = node
        while not cur.leaf:
            cur = cur.children[0]
        return cur.keys[0]

    def _fill(self, parent: BTreeNode, idx: int):
        # Borrow from previous sibling
        if idx > 0 and len(parent.children[idx - 1].keys) >= self.t:
            self._borrow_from_prev(parent, idx)
        # Borrow from next sibling
        elif idx < len(parent.children) - 1 and len(parent.children[idx + 1].keys) >= self.t:
            self._borrow_from_next(parent, idx)
        else:
            # Merge with a sibling
            if idx < len(parent.keys):
                self._merge(parent, idx)       # merge child idx with idx+1
            else:
                self._merge(parent, idx - 1)   # merge with previous sibling

    def _borrow_from_prev(self, parent: BTreeNode, idx: int):
        child = parent.children[idx]
        sibling = parent.children[idx - 1]

        # Move parent's key down to child (front)
        child.keys.insert(0, parent.keys[idx - 1])

        # If sibling is not leaf, move its last child to child's front
        if not child.leaf:
            child.children.insert(0, sibling.children.pop())

        # Move sibling's last key up to parent
        parent.keys[idx - 1] = sibling.keys.pop()

    def _borrow_from_next(self, parent: BTreeNode, idx: int):
        child = parent.children[idx]
        sibling = parent.children[idx + 1]

        # Move parent's key down to child (back)
        child.keys.append(parent.keys[idx])

        # If sibling is not leaf, move its first child to child's back
        if not child.leaf:
            child.children.append(sibling.children.pop(0))

        # Move sibling's first key up to parent
        parent.keys[idx] = sibling.keys.pop(0)

    def _merge(self, parent: BTreeNode, idx: int):
        """Merge child idx and idx+1 with parent.keys[idx] between them.
           Result stored in child idx; remove sibling and the key from parent.
        """
        child = parent.children[idx]
        sibling = parent.children[idx + 1]

        # Pull down parent key
        child.keys.append(parent.keys[idx])

        # Append sibling's keys
        child.keys.extend(sibling.keys)

        # Append sibling's children if any
        if not child.leaf:
            child.children.extend(sibling.children)

        # Remove key and sibling from parent
        parent.keys.pop(idx)
        parent.children.pop(idx + 1)

    # -----------------------
    # Traverse (in-order like for B-Tree)
    # -----------------------
    def traverse(self) -> List[int]:
        out: List[int] = []
        self._traverse(self.root, out)
        return out

    def _traverse(self, node: BTreeNode, out: List[int]):
        if node.leaf:
            out.extend(node.keys)
            return
        for i, k in enumerate(node.keys):
            self._traverse(node.children[i], out)
            out.append(k)
        self._traverse(node.children[-1], out)

# =========================================
# B-Tree Compact ASCII Printer
# =========================================

def display_btree_compact(node):
    """B-Tree를 Splay/AVL과 유사한 컴팩트 ASCII 형태로 출력."""
    lines, *_ = _btree_display_aux(node)
    for line in lines:
        print(line.rstrip())

def _btree_display_aux(node):
    """
    Returns: lines(list[str]), width(int), height(int), middle(int)
    - 노드 라벨: [k1|k2|...]
    - 자식 수가 N이면 N개의 서브블록을 좌→우로 나란히 붙이고, 부모를 위에 정렬.
    - 2번째 줄에 부모와 자식들을 '/' '\' '|'와 '_'로 연결선을 그림.
    """
    if node is None:
        return [" "], 1, 1, 0

    # 라벨: [k1|k2|...]
    s = "[" + "|".join(str(k) for k in node.keys) + "]"
    u = len(s)

    # 리프 노드면 그 자체를 반환
    if node.leaf or not node.children:
        return [s], u, 1, u // 2

    # 1) 각 자식 서브트리의 ASCII 블록 생성
    child_blocks = [ _btree_display_aux(c) for c in node.children ]
    child_lines_list, widths, heights, middles = zip(*child_blocks)

    # 2) 자식 블록들의 높이를 맞추기(짧은 쪽에 공백 라인 패딩)
    max_h = max(heights)
    padded_children = []
    for lines, w, h, m in child_blocks:
        if h < max_h:
            lines = lines + [" " * w] * (max_h - h)
        padded_children.append((lines, w, m))

    # 3) 자식 블록들을 가로로 이어붙이기(블록 사이 1칸 공백)
    gap = 1
    total_w = sum(w for _, w, _ in padded_children) + gap * (len(padded_children) - 1)
    merged_children_lines = []
    for row in range(max_h):
        row_parts = []
        for idx, (lines, w, m) in enumerate(padded_children):
            row_parts.append(lines[row])
            if idx != len(padded_children) - 1:
                row_parts.append(" " * gap)
        merged_children_lines.append("".join(row_parts))

    # 4) 부모 라벨과 자식 블록의 가로 정렬(중앙 정렬 느낌)
    if u < total_w:
        left_pad = (total_w - u) // 2
        right_pad = total_w - u - left_pad
        top_line = " " * left_pad + s + " " * right_pad
        width = total_w
        parent_middle = left_pad + u // 2
        # 자식들의 시작 x 좌표(왼쪽부터 누적)
        child_start_x = []
        cur_x = 0
        for i, (_, w, _) in enumerate(padded_children):
            child_start_x.append(cur_x)
            cur_x += w + (gap if i != len(padded_children) - 1 else 0)
    else:
        # 자식 블록이 좁다면 자식 쪽에 좌우 패딩을 추가해 부모 밑에 정렬
        pad_total = u - total_w
        left_pad = pad_total // 2
        right_pad = pad_total - left_pad
        merged_children_lines = [(" " * left_pad) + line + (" " * right_pad)
                                 for line in merged_children_lines]
        width = u
        top_line = s
        parent_middle = u // 2
        # 패딩을 반영한 자식 시작 x 좌표
        child_start_x = []
        cur_x = left_pad
        for i, (_, w, _) in enumerate(padded_children):
            child_start_x.append(cur_x)
            cur_x += w + (gap if i != len(padded_children) - 1 else 0)

    # 5) 부모-자식 연결선(두 번째 줄) 만들기
    #    - 첫/마지막 자식에는 '/' '\' 사용
    #    - 중간 자식들은 '|'로 표시
    conn = [" "] * width
    # 각 자식의 중앙 좌표
    child_centers = [ child_start_x[i] + padded_children[i][2] for i in range(len(padded_children)) ]

    for j, c in enumerate(child_centers):
        if c == parent_middle:
            conn[c] = '|'  # 바로 아래면 수직
        else:
            # 부모 중심에서 자식 중심까지 '_'로 연결
            lo, hi = sorted([c, parent_middle])
            for x in range(lo + 1, hi):
                conn[x] = '_' if conn[x] == " " else conn[x]
            # 자식 위치 문자
            if j == 0 and c < parent_middle:
                conn[c] = '/'
            elif j == len(child_centers) - 1 and c > parent_middle:
                conn[c] = '\\'
            else:
                conn[c] = '|'

    connector_line = "".join(conn)

    # 6) 최종 라인 병합
    lines = [top_line, connector_line] + merged_children_lines
    height = 2 + max_h
    return lines, width, height, parent_middle



# ===============================
# Example usage
# ===============================
if __name__ == "__main__":
    # Create a B-Tree of minimum degree t=3 (max 2t-1 = 5 keys per node)
    bt = BTree(t=3)

    # Insert a bunch of keys
    for k in [10, 20, 5, 6, 12, 30, 7, 17, 3, 2, 4, 15, 16, 18, 19, 21, 22, 23]:
        bt.insert(k)

    print("== Level-order view ==")
    display_btree_compact(bt.root)

    print("== Indented structure ==")
    display_btree_compact(bt.root)

    # Search tests
    for key in [6, 14, 23]:
        print(f"Search {key}: {'Found' if bt.search(key) else 'Not Found'}")

    print("\n== Traverse (sorted) ==")
    print(bt.traverse())

    # Delete tests
    for key in [6, 15, 10, 22, 3, 4, 5, 19, 23]:
        bt.delete(key)
        print(f"\n-- After delete {key} --")
        display_btree_compact(bt.root)
