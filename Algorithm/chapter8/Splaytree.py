# Splay tree implementation in Python
# splay tree 코드는 gpt를 활용하여 작성함.

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class SplayTree:
    def __init__(self):
        self.root = None

    # --- 회전 ---
    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    # --- 스플레이 연산 ---
    def _splay(self, root, key):
        if not root or root.key == key:
            return root

        # Case 1: key가 root의 왼쪽 서브트리에 있음
        if key < root.key:
            if not root.left:
                return root
            # Zig-Zig
            if key < root.left.key:
                root.left.left = self._splay(root.left.left, key)
                root = self._right_rotate(root)
            # Zig-Zag
            elif key > root.left.key:
                root.left.right = self._splay(root.left.right, key)
                if root.left.right:
                    root.left = self._left_rotate(root.left)
            return self._right_rotate(root) if root.left else root

        # Case 2: key가 root의 오른쪽 서브트리에 있음
        else:
            if not root.right:
                return root
            # Zig-Zig
            if key > root.right.key:
                root.right.right = self._splay(root.right.right, key)
                root = self._left_rotate(root)
            # Zig-Zag
            elif key < root.right.key:
                root.right.left = self._splay(root.right.left, key)
                if root.right.left:
                    root.right = self._right_rotate(root.right)
            return self._left_rotate(root) if root.right else root

    # --- 검색 ---
    def search(self, key):
        self.root = self._splay(self.root, key)
        return self.root and self.root.key == key

    # --- 삽입 ---
    def insert(self, key):
        if not self.root:
            self.root = Node(key)
            return
        self.root = self._splay(self.root, key)
        if self.root.key == key:
            return  # 이미 존재
        new_node = Node(key)
        if key < self.root.key:
            new_node.right = self.root
            new_node.left = self.root.left
            self.root.left = None
        else:
            new_node.left = self.root
            new_node.right = self.root.right
            self.root.right = None
        self.root = new_node

    # --- 삭제 ---
    def delete(self, key):
        if not self.root:
            return
        self.root = self._splay(self.root, key)
        if self.root.key != key:
            return  # 존재하지 않음
        if not self.root.left:
            self.root = self.root.right
        else:
            right_subtree = self.root.right
            self.root = self._splay(self.root.left, key)
            self.root.right = right_subtree

def display_tree(node):
    """Splay Tree를 2D 트리 형태로 예쁘게 출력"""
    lines, *_ = _display_aux(node)
    for line in lines:
        print(line)


def _display_aux(node):
    """Returns list of strings, width, height, and horizontal coordinate of the root."""
    if node is None:
        return [" "], 1, 1, 0

    s = str(node.key)
    u = len(s)

    # --- Case 1: no child ---
    if node.left is None and node.right is None:
        width = u
        height_lines = 1
        middle = u // 2
        return [s], width, height_lines, middle

    # --- Case 2: only left child ---
    if node.right is None:
        left_lines, n, p, x = _display_aux(node.left)
        first_line  = (x + 1) * " " + (n - x - 1) * "_" + s
        second_line =  x      * " "  + "/"                + (n - x - 1 + u) * " "
        shifted     = [line + u * " " for line in left_lines]
        return [first_line, second_line] + shifted, n + u, p + 2, n + u // 2

    # --- Case 3: only right child ---
    if node.left is None:
        right_lines, n, p, x = _display_aux(node.right)
        first_line  = s + x * "_" + (n - x) * " "
        second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
        shifted     = [u * " " + line for line in right_lines]
        return [first_line, second_line] + shifted, n + u, p + 2, u // 2

    # --- Case 4: both children ---
    left_lines,  n, p, x = _display_aux(node.left)
    right_lines, m, q, y = _display_aux(node.right)

    first_line  = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
    second_line =  x      * " "  + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "

    if p < q:
        left_lines  += [" " * n] * (q - p)
    elif q < p:
        right_lines += [" " * m] * (p - q)

    lines = [a + u * " " + b for a, b in zip(left_lines, right_lines)]
    return [first_line, second_line] + lines, n + m + u, max(p, q) + 2, n + u // 2


# ======================================
# 실행 예시
# ======================================
if __name__ == "__main__":
    splay_tree = SplayTree()
    values = [10, 20, 30, 40, 50, 25]
    for val in values:
        splay_tree.insert(val)

    print("Splay Tree 구조:")
    display_tree(splay_tree.root)

    print("\nSearch 50 후 구조:")
    splay_tree.search(50)
    display_tree(splay_tree.root)

    print("\nDelete 20 후 구조:")
    splay_tree.delete(20)
    display_tree(splay_tree.root)