# AVL Tree implementation in Python

# Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # 리프의 높이 = 1

# 유틸리티: 노드 높이 계산
def height(node):
    return node.height if node else 0

# 유틸리티: 노드 높이 업데이트(국소 갱신)
def update_height(node):
    node.height = 1 + max(height(node.left), height(node.right))
    return node

# 유틸리티: 균형 인자(왼-오)
def balance_factor(node):
    return height(node.left) - height(node.right) if node else 0

# AVL Tree class
class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            # 중복은 오른쪽으로 넣는 정책(필요하면 == 분기 따로)
            node.right = self._insert(node.right, value)

        # 리턴 단계: 국소적으로 높이 갱신 후 재균형
        update_height(node)
        return self._rebalance(node)

    # ---- Rebalance & Rotations ----
    def _rebalance(self, node):
        bf = balance_factor(node)

        # Left heavy
        if bf > 1:
            # LR: 왼자식이 Right-heavy면 먼저 왼자식 좌회전
            if balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Right heavy
        if bf < -1:
            # RL: 오른자식이 Left-heavy면 먼저 오른자식 우회전
            if balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node  # 균형이면 그대로

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        # 회전
        y.left = z
        z.right = T2

        # 높이 국소 갱신(자식 z 먼저, 그 다음 y)
        update_height(z)
        update_height(y)
        return y

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        # 회전
        y.right = z
        z.left = T3

        # 높이 국소 갱신(자식 z 먼저, 그 다음 y)
        update_height(z)
        update_height(y)
        return y
    
    # ---- Search ----
    def search(self, value):
        return self._contains(self.root, value)

    def _contains(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._contains(node.left, value)
        else:
            return self._contains(node.right, value)

    # ---- Deletion ----
    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return node
        if not self._contains(node, value):
            print(f"Value {value} not found in the tree.")
            return node

        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            # 노드 찾음
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # 두 자식 모두 있을 때: 오른쪽 서브트리에서 최소값 찾기
                min_larger_node = self._get_min(node.right)
                node.value = min_larger_node.value
                node.right = self._delete(node.right, min_larger_node.value)

        # 리턴 단계: 국소적으로 높이 갱신 후 재균형
        update_height(node)
        return self._rebalance(node)
    
    # 유틸리티: 서브트리에서 최소값 노드 찾기
    def _get_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    # traversal (in-order)
    def inorder(self):
        return self._inorder(self.root)
    
    def _inorder(self, node):
        if node is None:
            return []
        return self._inorder(node.left) + [node.value] + self._inorder(node.right)

if __name__ == "__main__":

    # ---- 트리 모양 + (height, bf) 표기 ----
    def display_tree(node, show_height=True, show_bf=True):
        """AVL 트리를 2D 형태로 예쁘게 출력 (예: 3(h=2, bf=0))"""
        lines, *_ = _display_aux_labeled(node, show_height, show_bf)
        for line in lines:
            print(line)

    def _node_label(n, show_height, show_bf):
        if n is None:
            return " "
        parts = [str(n.value)]
        if show_height:
            parts.append(f"h={n.height}")
        if show_bf:
            parts.append(f"bf={balance_factor(n)}")
        return f"{parts[0]}(" + ", ".join(parts[1:]) + ")" if len(parts) > 1 else parts[0]

    def _display_aux_labeled(node, show_height, show_bf):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        if node is None:
            return [" "], 1, 1, 0

        s = _node_label(node, show_height, show_bf)
        u = len(s)

        # --- Case 1: no child ---
        if node.left is None and node.right is None:
            width = u
            height_lines = 1
            middle = u // 2
            return [s], width, height_lines, middle

        # --- Case 2: only left child ---
        if node.right is None:
            left_lines, n, p, x = _display_aux_labeled(node.left, show_height, show_bf)
            first_line  = (x + 1) * " " + (n - x - 1) * "_" + s
            second_line =  x      * " "  + "/"                + (n - x - 1 + u) * " "
            shifted     = [line + u * " " for line in left_lines]
            return [first_line, second_line] + shifted, n + u, p + 2, n + u // 2

        # --- Case 3: only right child ---
        if node.left is None:
            right_lines, n, p, x = _display_aux_labeled(node.right, show_height, show_bf)
            first_line  = s + x * "_" + (n - x) * " "
            second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
            shifted     = [u * " " + line for line in right_lines]
            return [first_line, second_line] + shifted, n + u, p + 2, u // 2

        # --- Case 4: both children ---
        left_lines,  n, p, x = _display_aux_labeled(node.left,  show_height, show_bf)
        right_lines, m, q, y = _display_aux_labeled(node.right, show_height, show_bf)

        first_line  = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
        second_line =  x      * " "  + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "

        if p < q:
            left_lines  += [" " * n] * (q - p)
        elif q < p:
            right_lines += [" " * m] * (p - q)

        lines = [a + u * " " + b for a, b in zip(left_lines, right_lines)]
        return [first_line, second_line] + lines, n + m + u, max(p, q) + 2, n + u // 2


    avl = AVLTree()
    values = [10, 20, 30, 40, 50, 25]

    for val in values:
        avl.insert(val)

    print("AVL Tree constructed with values:", values)
    display_tree(avl.root)

    search_vals = [25, 60]
    for val in search_vals:
        found = avl.search(val)
        print(f"Search {val}: {'Found' if found else 'Not Found'}")

    delete_vals = [10, 20]
    for val in delete_vals:
        avl.delete(val)
        print(f"Deleted {val} from AVL Tree.")

    print("In-order traversal after deletions:", avl.inorder())
    display_tree(avl.root)
